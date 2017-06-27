from .model.customers import Customers
from .model.image import ImageUpload
from .model.order import Orders
from .model.site_visit import SiteVisits
import heapq

from src.mapper.customers_mapper import CustomersMapper
from src.mapper.order_mapper import OrderMapper
from src.mapper.image_mapper import ImageMapper
from src.mapper.site_visit_mapper import SiteVisitMapper

from src.data_store.customer_data import CustomerData
from src.data_store.order_data import OrderData
from src.data_store.site_visit_data import SiteVisitDataStore
from src.data_store.image_data import ImageData


class EventMapper(object):
    '''
    Class creates in-memory data structure
    and evaluates top x valued customers
    using simple ltv
    '''
    event_mapper = {"CUSTOMER": (Customers, CustomersMapper, CustomerData), # noqa
                  "SITE_VISIT": (SiteVisits, SiteVisitMapper, SiteVisitDataStore), # noqa
                  "ORDER": (Orders, OrderMapper,OrderData), # noqa
                  "IMAGE": (ImageUpload, ImageMapper, ImageData)} # noqa

    def __init__(self, logger=None):
        self.logger = logger
        # For shutterfly value of t is given by 10
        self.t = 10

    # Ingest event e and assigns it to in-memory data structure D
    def Ingest(self, e, D):

        event_name = e["type"]
        self.logger.info(e)
        if(event_name in self.event_mapper):
            mapper_object = self.event_mapper[event_name][1]
            self.logger.debug(event_name)
            val = mapper_object.map_to_model(e,
                                             self.event_mapper[event_name][0]()
                                             )
            data_store = self.event_mapper[event_name][2]
            data_store.add_data(val, D)

    def TopXSimpleLTVCustomers(self, x, D):

        top_valued_customers = list()
        customer_data = self.event_mapper["CUSTOMER"][2].get_data(D)
        order_data = self.event_mapper["ORDER"][2].get_data(D)
        site_visit_data = self.event_mapper["SITE_VISIT"][2].get_data(D)

        ltv_customer = []

        for customer_id in customer_data.keys():

            if customer_id in order_data and customer_id in site_visit_data:

                total_amount = order_data[customer_id]["total_amount"]
                total_visit = site_visit_data[customer_id]["site_visit"]
                customer_expenditures_per_visit = float(total_amount) \
                    / float(total_visit)
                number_of_site_visits_per_week = float(total_visit)/float(52)

                a = customer_expenditures_per_visit * \
                    number_of_site_visits_per_week

                ltv = 52 * a * self.t
                self.logger.info("ltv value: " + str(ltv) + " customer id: "
                                 + customer_id)
                heapq.heappush(ltv_customer, (ltv,  customer_id))

        customers = heapq.nlargest(x, ltv_customer)

        for customer in customers:
            top_valued_customers.append(customer[1])

        return top_valued_customers
