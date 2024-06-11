# Diplom_3 
Сайт: https://stellarburgers.nomoreparties.site/ 

Для запуска теста используйте команду:  
pytest --browser=chrome tests/test_check_main_functions.py tests/test_order_feed_page.py tests/test_personal_account.py tests/test_recovery_password.py      

Для составления отчета используйте:  
pytest --browser=chrome tests/test_check_main_functions.py tests/test_order_feed_page.py tests/test_personal_account.py tests/test_recovery_password.py --alluredir=allure_result

Для просмотра отчёта:  
allure serve allure_results