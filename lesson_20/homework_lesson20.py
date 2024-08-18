import psycopg2


class PostgresConnector:
    def __init__(self, dbname='test_bd', user='yuliiaudovichenko', password=123, host='localhost', port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def __enter__(self):
        print('__enter__ method')
        self.connection = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__ method')
        self.connection.commit()
        self.cursor.close()
        self.connection.close()


class PostgresExecutor():
    def __init__(self):
        self.db = PostgresConnector

    def create_table_categories(self):
        with self.db() as cursor:
            cursor.execute('''CREATE TABLE public.categories (id int4 NOT NULL, 
            "name" varchar NOT NULL, CONSTRAINT categories_pk PRIMARY KEY (id));''')
            cursor.execute('''INSERT INTO public.categories (id, "name") values (10, 'movies'), (20, 'cartoons'), 
            (30, 'serials'), (40, 'documentaries')''')
            cursor.execute('select * from public.categories')
            categories_result = cursor.fetchall()
            print(categories_result)

    def create_table_products(self):
        with self.db() as cursor:
            cursor.execute('''CREATE TABLE public.products (id int4 NOT NULL, "name" varchar NOT NULL,
            "description" varchar NOT NULL, price DECIMAL(10, 2) NOT NULL, categories_id int4 NULL,
            CONSTRAINT products_pk PRIMARY KEY (id),
            CONSTRAINT products_categories_fk FOREIGN KEY (categories_id) REFERENCES public."categories"(id));''')
            cursor.execute('''INSERT INTO public.products (id, "name", "description", price, categories_id) 
            values (1, 'The Queens Gambit', 'chess, talent, competition', 350, 30), 
            (2, 'Stone Men', 'Marble is the most luxurious stone in the world', 575, 40);''')
            cursor.execute('select * from public.products')
            products_result = cursor.fetchall()
            print(products_result)

    def join_tables(self):
        with self.db() as cursor:
            cursor.execute('''SELECT p.name as product_name, p.description as about_product, 
            p.price as rent_price, c.name as category_name
            FROM public.products p
            JOIN public.categories c on p.categories_id = c.id;''')
            joined_result = cursor.fetchall()
            print("Joined Tables Result:")
            print(joined_result)


executor = PostgresExecutor()
executor.create_table_categories()
executor.create_table_products()
executor.join_tables()