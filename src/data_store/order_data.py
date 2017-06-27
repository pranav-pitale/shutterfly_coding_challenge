from src.data_store.base_data_store import BaseDataStore


class OrderData(BaseDataStore):
    '''
    Data structure for storing order data
    '''

    # Adds data to order data structure
    @staticmethod
    def add_data(event, D):
        order_value = dict()

        if event.customer_id not in D.orders:
            order_value["object"] = [event]
            order_value["total_amount"] = float(
                event.total_amount.split(' ')[0].strip())

            D.orders[event.customer_id] = order_value

        else:
            order_value = D.orders[event.customer_id]
            objectList = order_value['object']
            objectList.append(event)
            order_value['total_amount'] += float(
                event.total_amount.split(' ')[0].strip())
            D.orders[event.customer_id] = order_value

    # Gets data from order data structure
    @staticmethod
    def get_data(D):
        return D.orders
