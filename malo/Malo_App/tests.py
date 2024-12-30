from django import test
from django.forms import Select
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


# Create your tests here.

class TestHome(LiveServerTestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://127.0.0.1:8000/')

    def test2CriarLoginGarcom1(self):
        self.driver.find_element(By.ID,"signup").click()
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, 'username').send_keys('Garcom1')
        self.driver.find_element(By.CLASS_NAME, 'email').send_keys('garcom1@malo.com')
        self.driver.find_element(By.CLASS_NAME, 'password1').send_keys('Senhamassa')
        self.driver.find_element(By.CLASS_NAME, 'password2').send_keys('Senhamassa')
        self.driver.find_element(By.CLASS_NAME, 'submit').submit()
        

    def Login(self):
        self.setUp()

        self.driver.find_element(By.NAME, 'username').send_keys('Gerente')
        self.driver.find_element(By.NAME, 'password').send_keys('Senhamassa')
        self.driver.find_element(By.CLASS_NAME, 'login').click()
        time.sleep(5)


    def testLoginGerente(self):
        self.Login()

        curl = self.driver.current_url
        print(curl)
        if '/home/' in curl:
            return 'User logged in'
        else:
            return 'User not logged in'
       
    def testOpenMesa(self): 
        self.Login()
        omesa = self.driver.find_element(By.CLASS_NAME, 'mesa')
        assert omesa.get_attribute('href') == "http://127.0.0.1:8000/mesa/"

    
    def testAdd1Mesa(self): 
        self.Login()
        self.driver.find_element(By.CLASS_NAME, 'mesa').click()
        self.driver.find_element(By.CLASS_NAME, 'add_mesa').click()


    def testAddMultMesas(self): 
        self.Login()
        self.driver.find_element(By.CLASS_NAME, 'mesa').click()
        self.driver.find_element(By.ID, 'add_qtd_mesas').send_keys('4')
        self.driver.find_element(By.CLASS_NAME, 'submit_add_mesas').click()

    def testRem1Mesa(self): 
        self.Login()
        self.driver.find_element(By.CLASS_NAME, 'mesa').click()
        self.driver.find_element(By.ID, 'rem_mesa').click()


    def testRemMultMesas(self): 
        self.Login()
        self.driver.find_element(By.CLASS_NAME, 'mesa').click()
        self.driver.find_element(By.ID, 'rem_qtd_mesas').send_keys('2')
        self.driver.find_element(By.CLASS_NAME, 'submit_rem_mesas').click()

    def test3AddCategory1(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "menu_category").click()
        self.driver.find_element(By.CLASS_NAME, 'add_category').click()
        self.driver.find_element(By.CLASS_NAME, 'categoria').send_keys('Jantar')
        self.driver.find_element(By.CLASS_NAME, 'enviar').click()

    
    def testAddCategory2(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')
        self.driver.find_element(By.CLASS_NAME, 'menu_category').click()
        self.driver.find_element(By.CLASS_NAME, 'add_category').click()
        self.driver.find_element(By.CLASS_NAME, 'categoria').send_keys('Comidas')
        self.driver.find_element(By.CLASS_NAME, 'enviar').click()

    def test3EditCategory(self): 
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')
        self.driver.find_element(By.CLASS_NAME, 'menu_category').click()
        self.driver.find_element(By.CLASS_NAME, 'edit_Sobremesas').click()
        self.driver.find_element(By.CLASS_NAME, 'categoria').clear()
        self.driver.find_element(By.CLASS_NAME, 'categoria').send_keys('Bebidas Lacteas')

        self.driver.find_element(By.CLASS_NAME, 'submit').click()
  
        
    def testRemCategoryTemp(self): 
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')
        self.driver.find_element(By.CLASS_NAME, 'menu_category').click()
        self.driver.get('http://127.0.0.1:8000/delete-category/3')
     
    def testAddDish(self): 
        self.Login()
        self.driver.get('http://127.0.0.1:8000/add-dishes/')
        elemento_select = self.driver.find_element(By.NAME, "category")

        dropdown = Select(elemento_select)
        elemento_select.click()
        dropdown.select_by_visible_text("Almoços")

        self.driver.find_element(By.NAME, 'name').send_keys('Macarronada')
        self.driver.find_element(By.NAME, 'price').send_keys('60')
        self.driver.find_element(By.NAME, 'description').send_keys('Serve até 4 pessoas')       
        submit_button = self.driver.find_element(By.CLASS_NAME, 'submit')
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        time.sleep(2)
        submit_button.click()
  

    
    def testEditDish(self): #error
        self.Login()
        self.driver.get('http://127.0.0.1:8000/menu-category/')
        self.driver.find_element(By.NAME, 'edit_Suco de Laranja').click()
        elemento_select = self.driver.find_element(By.NAME, "category")

        dropdown = Select(elemento_select)
        elemento_select.click()
        dropdown.select_by_visible_text("Bebidas")

        self.driver.find_element(By.NAME, 'price').clear()
        self.driver.find_element(By.NAME, 'price').send_keys('12')
        submit_button = self.driver.find_element(By.CLASS_NAME, 'submit')
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        time.sleep(2)
        submit_button.click()
    
    def testEditCategoryDish(self): 
        self.Login()
        self.driver.get('http://127.0.0.1:8000/menu-category/') 
        self.driver.find_element(By.CLASS_NAME, 'edit_Bebidas').click()
        self.driver.find_element(By.ID, 'dish_Arroz com ovo').click()
        self.driver.find_element(By.CLASS_NAME, 'submit').click()
        self.driver.find_element(By.CLASS_NAME, 'edit_Almoços').click()
        self.driver.find_element(By.ID, 'dish_Arroz com ovo').click()
        self.driver.find_element(By.CLASS_NAME, 'submit').click()
                    


    def testOpenMenu(self): 
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')
        menu = self.driver.find_element(By.CLASS_NAME, 'menu_category')
        assert menu.get_attribute('href') == "http://127.0.0.1:8000/menu-category/"


    def testOpenIgredient(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')

        ingredient_list = self.driver.find_element(By.CLASS_NAME, 'ingredient_list')
        assert ingredient_list.get_attribute('href') == "http://127.0.0.1:8000/ingredient-list/"
      
    def testAddIgredient(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/add-ingredientes/')
        self.driver.find_element(By.NAME, 'name').send_keys('Laranja')
        self.driver.find_element(By.NAME, 'exp_date').send_keys('18/05/2023')
        self.driver.find_element(By.NAME, 'quantity').send_keys('5')
        self.driver.find_element(By.NAME, 'measure_unit').send_keys('Unidades')
        self.driver.find_element(By.NAME, 'price').send_keys('5')
        self.driver.find_element(By.NAME, 'obs').send_keys('Laranjas para suco e refrigerante(em rodelas)')
        self.driver.find_element(By.CLASS_NAME, 'submit').submit()

    def testOpenMenuList(self): 
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')
        self.driver.find_element(By.CLASS_NAME, 'menu_category').click()
        menu = self.driver.find_element(By.CLASS_NAME, 'menu')
        assert menu.get_attribute('href') == "http://127.0.0.1:8000/menu/"
        
    def testOpenAddCategory(self): 
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')
        self.driver.find_element(By.CLASS_NAME, 'menu_category').click()
        oaddcat = self.driver.find_element(By.CLASS_NAME, 'add_category')
        assert oaddcat.get_attribute('href') == "http://127.0.0.1:8000/add-category/"

    

    def testLogout(self):
        self.Login()
        logout = self.driver.find_element(By.CLASS_NAME, 'logout')
        assert logout.get_attribute('href') == "http://127.0.0.1:8000/logout/"
        print(self.testLoginGerente())

    def testViewFat(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')

        submit_button = self.driver.find_element(By.CLASS_NAME, 'invoice_list')
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        time.sleep(2)
        submit_button.click()
        

    def testSetGarcom(self):
        self.Login()
        self.driver.get('http://127.0.0.1:8000/home/')
        self.driver.find_element(By.CLASS_NAME, 'garcom_list').click()
        self.driver.find_element(By.CLASS_NAME, 'add-garcom').click()
        self.driver.find_element(By.NAME, 'nome').send_keys('Marcelo')

        elemento_select = self.driver.find_element(By.NAME, "cargo")
        dropdown = Select(elemento_select)
        elemento_select.click()
        dropdown.select_by_visible_text("garçom")

        self.driver.find_element(By.NAME, 'salario').send_keys('1800')

        elemento_select = self.driver.find_element(By.NAME, "login")
        dropdown = Select(elemento_select)
        elemento_select.click()
        dropdown.select_by_visible_text("Marcelo")
        
        self.driver.find_element(By.CLASS_NAME, 'enviar-funcionario').click()
        

    def LoginGarcom(self):
        self.setUp()

        self.driver.find_element(By.NAME, 'username').send_keys('Jorge')
        self.driver.find_element(By.NAME, 'password').send_keys('Senhamassa')
        self.driver.find_element(By.CLASS_NAME, 'login').click()

    def testLoginGarcom(self):
        self.LoginGarcom()

        curl = self.driver.current_url
        print(curl)
        if '/home-garcom/' in curl:
            return 'Jorge logged in'
        else:
            return 'Jorge not logged in'

    def testGarcomCreateOrder(self):
        self.LoginGarcom()
        self.driver.find_element(By.NAME, 'Mesa 1').click()
        self.driver.find_element(By.CLASS_NAME, 'Fazer-pedido').click()

        elemento_select = self.driver.find_element(By.NAME, "dish")
        dropdown = Select(elemento_select)
        elemento_select.click()
        dropdown.select_by_visible_text("Sorvete de Baunilha")

        self.driver.find_element(By.NAME, 'quantity').clear()
        self.driver.find_element(By.NAME, 'quantity').send_keys('2')
        self.driver.find_element(By.NAME, 'obs').send_keys('Após almoço') 
        self.driver.find_element(By.CLASS_NAME, 'submit').click()

    def testGarcomConfirmOrder(self):
        self.LoginGarcom()
        self.driver.find_element(By.NAME, 'Mesa 2').click()      
        self.driver.find_element(By.NAME, 'Fechar-conta').click()
        self.driver.find_element(By.CLASS_NAME, 'close-order').click()



    def tearDown(self):
        self.driver.quit() 