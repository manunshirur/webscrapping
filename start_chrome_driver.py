import contextlib
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui
import pandas as pd



with contextlib.closing(webdriver.Chrome()) as driver:
    # URL of the website
    URL = "https://iquest.siu.edu/program_review/course_enrollments_by_semester.php"

    # Get Chrome Driver 
    driver.get(URL)

    # Dropdown value of the `name` property
    dropdown_name = 'College'

    # Dropdown option value 
    dropdown_option_value = 'AP-Applied Sciences & Arts'

    # Select the required option from the dropdown
    select = Select(driver.find_element_by_name(dropdown_name))
    select.select_by_value(dropdown_option_value)



    # Submit Button's name
    submit_button_name = 'Submit'

    # Click the submit button 
    driver.find_element_by_name(submit_button_name).click()

    # Table id
    table_id = 'enroll'

    # Wait for the table to get generated after submit
    wait_time_in_sec = 10
    wait = ui.WebDriverWait(driver, wait_time_in_sec)
    wait.until(lambda driver: driver.find_element_by_id(table_id))
    
    # Table id
    table_body_xpath = '//*[@id="enroll"]/tbody'

    table_id = driver.find_element_by_xpath(table_body_xpath)

    # Get all the rows of the table
    rows = table_id.find_elements_by_tag_name("tr")

    # Dataframe
    df = pd.DataFrame()
    for row in rows:
        # Get the columns     
        college = row.find_elements_by_tag_name("td")[0] 
        department = row.find_elements_by_tag_name("td")[1] 
        course_title = row.find_elements_by_tag_name("td")[2] 
        course_id = row.find_elements_by_tag_name("td")[3] 
        section = row.find_elements_by_tag_name("td")[4] 
        course_level = row.find_elements_by_tag_name("td")[5] 
        course_hours = row.find_elements_by_tag_name("td")[6] 
        instructor = row.find_elements_by_tag_name("td")[7] 
        course_enrollment = row.find_elements_by_tag_name("td")[8]
        df = df.append(pd.DataFrame({'college': college.text, 'department': department.text, 
            'course_title': course_title.text, 'course_id': course_id.text, 'section': section.text,
            'course_level': course_level.text, 'course_hours': course_hours.text, 'instructor': instructor.text, 
            'course_enrollment': course_enrollment.text}, index=[0]), ignore_index=True)
        # print(college.text, department.text, course_title.text, course_id.text, 
            #section.text, course_level.text, course_hours.text, instructor.text, 
            #course_enrollment.text )#prints text from the element
    #df.to_csv(r'course_enrollement.csv', index = False, header=True)   