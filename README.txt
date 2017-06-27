Shutterfly assessment:


Classes and Pakages:
  
  model: Holds the models for representation of an event
    - customers.py : Model for customer event
    - order.py : Model for order event
    - image.py : Model for image upload event
    - site_visit : Model for site_visit event

  mapper : Helps to map events to its models
    - base.py : Abstract base class for mapping events to its model
    - customers_mapper.py : class for mapping customer event to its model
    - order_mapper.py : class for mapping order event to its model
    - image_mapper.py : class for mapping image event to its model
    - site_visit_mapper.py : class for mapping site_visit event to its model

  util : Its an utily package performing different function
    - date_util : It has get_weeks method which calculates number of weeks of data set
    - file_process : It performs read and write operations
    - logger : Helps in logging 
    - remove_unicode : Removes unicode from the string

  data_store : Stores in-memory data-structure for the operations
    - base_data_store : Abstract base class for adding event model to data structure
    - customer_data : Stores events objects of customers
    - image_data : Stores events objects of image event
    - order_data : Stores events objects of order event
    - site_visit : Stores events objects of site_visit event
    - data_store : In-memory data structre to hold objects of all events    

  driver.py: It has main method

  event_mapper.py : It Ingest method and TopXLTV method
    -Ingest(e, D) : Reads event e, maps to particular model depending on event,
                    Add events to In-memory data-structure DataStore
    - TopXSimpleLTVCustomers( x, D):  Calculate simple ltv value of customers, returns top x
                                      customers depending on ltv value


Run and compile:
  By using Docker:
    - Install docker and docker-compose on your machine
    - If your using windows machine enable Hyper-V settings and enable shared drive setting in
      Docker setting for drive in which your placing your source code. For linux or MacOS machines
      skip these step.
    - run following in root "docker-compose build" of your src where DockerFile resides
    - "docker-compose up"
    - " docker-compose run shutterfly-assessment bash"
    - cd src
    - python driver.py 

Input_file:
  Default input_file path : ../input/input.txt
    - python -m driver --file file_path

Output file:
    Default output_file path : ../output/output.txt
    - python -m driver --output file_path

TopXLTV:
  Default value is 2
  - python -m driver --topxltv 10 : Return top 10 customers based on ltv value

tests: It has test case
  - cd tests
  - pytest  
  - pytest --cov

