import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.LoginPage import LoginPage
from pageobjects.RegisterPage import RegisterPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_website(self):
        return self.driver.get("https://www.opencart.com/")

    def check_main_page_title(self):
        assert self.driver.title.__eq__("OpenCart - Open Source Shopping Cart Solution")

    def check_main_page_url(self):
        assert self.driver.current_url == "https://www.opencart.com/index.php?route=common/home"

    def get_opencart_logo(self):
        return self.driver.find_element(By.XPATH,"//img[@title='OpenCart - Open Source Shopping Cart Solution']")

    def get_opencart_logo_from_feature_page(self):
        return self.driver.find_element(By.XPATH,"//img[@title='OpenCart - Features']")

    def get_opencart_logo_from_demo_page(self):
        return self.driver.find_element(By.XPATH,"//img[@title='OpenCart - Demo']")

    def get_opencart_logo_from_marketplace_page(self):
        return self.driver.find_element(By.XPATH,"//img[@title='Opencart extensions']")

    def get_opencart_logo_from_blog_page(self):
        return self.driver.find_element(By.XPATH,"//img[@title='OpenCart - Blog']")

    def get_opencart_logo_from_download_page(self):
        return self.driver.find_element(By.XPATH,"//img[@title='OpenCart - Downloads']")

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, "//a[@class='btn btn-link navbar-btn']")

    def click_login_button(self):
        self.get_login_button().click()

    def get_register_option(self):
        return self.driver.find_element(By.XPATH ,"//a[@class='btn btn-black navbar-btn']")

    def click_register_button(self):
        self.get_register_option().click()

    def get_account_option(self):
        return self.driver.find_element(By.XPATH, "//a[@class='btn btn-link navbar-btn']")

    def click_account_option(self):
        self.get_account_option().click()

    def check_account_page(self):
        assert self.driver.find_element(By.XPATH, "//p[text()='Welcome to OpenCart!']").is_displayed()

    def get_logout_option(self):
        return self.driver.find_element(By.XPATH ,"//a[@class='btn btn-black navbar-btn']")

    def click_logout_option(self):
        self.get_logout_option().click()

    def check_logout_page(self):
        assert self.driver.title == "OpenCart - Open Source Shopping Cart Solution"

    def get_feature_option(self):
        return self.driver.find_element(By.XPATH
                                        ,"//ul[@class='nav navbar-nav']//a[normalize-space()='Features']")

    def click_feature_option(self):
        self.get_feature_option().click()

    def check_feature_page(self):
        assert self.driver.title == "OpenCart - Features"

    def get_demo_option(self):
        return self.driver.find_element(By.XPATH, "//ul[@class='nav navbar-nav']//a[normalize-space()='Demo']")

    def click_demo_option(self):
        self.get_demo_option().click()

    def check_demo_page(self):
        assert self.driver.title == "OpenCart - Demo"

    def get_marketplace_option(self):
        return self.driver.find_element(By.XPATH
                                        ,"//ul[@class='nav navbar-nav']//a[normalize-space()='Marketplace']")

    def click_marketplace_option(self):
        self.get_marketplace_option().click()

    def check_marketplace_page(self):
        assert self.driver.title == "Opencart extensions"

    def get_blog_option(self):
        return self.driver.find_element(By.XPATH,"//a[normalize-space()='Blog']")

    def click_blog_option(self):
        self.get_blog_option().click()

    def check_blog_page(self):
        assert self.driver.title == "OpenCart - Blog"

    def get_download_option(self):
        return self.driver.find_element(By.XPATH
                                        ,"//ul[@class='nav navbar-nav']//a[normalize-space()='Download']")

    def click_download_option(self):
        self.get_download_option().click()

    def check_download_page(self):
        assert self.driver.title.__eq__("OpenCart - Downloads")

    def get_resources_developer_option(self):
        self.driver.find_element(By.XPATH, "//li[@class='dropdown']/a").click()
        return self.driver.find_element(By.XPATH, "//ul[@class='dropdown-menu']/li[9]/a")

    def click_resources_developer_option(self):
        self.get_resources_developer_option().click()

    def check_resources_developer_page(self):
        assert self.driver.title == "OpenCart Documentation"

    def check_header_ui(self):
        element1 = self.driver.find_element(By.ID, "navbar-collapse-header")
        assert element1.value_of_css_property("font-size").__eq__("16px")
        assert element1.value_of_css_property("line-height").__eq__("25.6px")

    def check_logo_ui(self):
        element2 = self.driver.find_element(By.XPATH, "/html/body/header/nav/div/div[1]/a/img")
        assert element2.value_of_css_property("margin-top").__eq__("21px")
        assert element2.value_of_css_property("height").__eq__("36px")

    def check_hero_section_image(self):
        image = self.driver.find_element(By.XPATH, "//div[@class='device hidden-xs hidden-sm']")
        # get the position and size of the image element
        location = image.location
        size = image.size
        # check if the image is within the viewport of the browser window
        viewport_height = self.driver.execute_script("return window.innerHeight;")
        assert 0 <= location['y'] <= viewport_height

    def check_hero_section_ui(self):
        element = self.driver.find_element(By.XPATH, "//div[@id='hero']/div/div/div")
        assert element.value_of_css_property("font-size").__eq__("16px")
        assert element.value_of_css_property("padding-left").__eq__("15px")
        assert element.value_of_css_property("padding-right").__eq__("15px")

    def check_resize_of_image_hero_section(self):
        def changing(x, y):
            self.driver.set_window_size(x, y)
            # wait for the page to load
            #time.sleep(3)
            image = self.driver.find_element(By.XPATH, "//div[@class='device hidden-xs hidden-sm']")
            # get the position and size of the image element
            location = image.location
            size = image.size
            # check if the image is within the viewport of the browser window
            viewport_height = self.driver.execute_script("return window.innerHeight;")
            assert 0 <= location['y'] <= viewport_height

        changing(100, 500)
        changing(200, 700)
        changing(300, 500)
        changing(400, 400)
        changing(500, 900)
        changing(600, 400)
        changing(800, 600)
        changing(1000, 500)

    def get_free_download_option(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Free Download']")

    def click_free_download_option(self):
        self.get_free_download_option().click()

    def get_view_demo_option(self):
        return self.driver.find_element(By.XPATH,"//*[@id='hero']/div[1]/div[1]/div/p[2]/a[2]")

    def click_view_demo_option(self):
        self.get_view_demo_option().click()

    def get_previous_page(self):
        self.driver.back()

    def check_content_section_ui(self):
        element = self.driver.find_element(By.ID, "common-home")
        assert element.value_of_css_property("font-size").__eq__("16px")
        assert element.value_of_css_property("line-height").__eq__("25.6px")

    def check_resize_of_content_section(self):
        def changing(x, y):
            self.driver.set_window_size(x, y)
            # wait for the page to load
            #time.sleep(3)
            element = self.driver.find_element(By.XPATH, "//div[@id='common-home']")
            # get the position and size of the image element
            location = element.location
            size = element.size
            # check if the image is within the viewport of the browser window
            viewport_height = self.driver.execute_script("return window.innerHeight;")
            assert 0 <= location['y'] <= viewport_height

        changing(100, 500)
        changing(200, 700)
        changing(300, 500)
        changing(400, 400)
        changing(500, 900)
        changing(600, 400)
        changing(800, 600)
        changing(1000, 500)

    def get_section_two(self):
        return self.driver.find_element(By.ID, "business")

    def click_british_red_cross_logo(self):
        self.driver.find_element(By.XPATH,"//img[@src='application/view/image/home/brand/british-red-cross.png']").click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_british_red_cross_website(self):
        assert self.driver.title == "Shop charity gifts | British Red Cross Gift Shop"
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_penn_logo(self):
        self.driver.find_element(By.XPATH, "//img[@src='application/view/image/home/brand/bjpenn.com.png']").click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_penn_website(self):
        assert self.driver.current_url.__eq__("https://shop.bjpenn.com/")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_concordia_college_logo(self):
        self.driver.find_element(By.XPATH, "//img[@src='application/view/image/home/brand/concordia-college.png']").click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_concordia_college_website(self):
        assert self.driver.current_url.__eq__("https://shop.concordia-ny.edu/")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_fx_creations_logo(self):
        self.driver.find_element(By.XPATH, "//img[@src='application/view/image/home/brand/fx-creation.png']").click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_fx_creations_website(self):
        assert self.driver.current_url.__eq__("https://fxcreations.com/")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_hku_logo(self):
        self.driver.find_element(By.XPATH, "//img[@src='application/view/image/home/brand/hkuvcg.png']").click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_hku_website(self):
        assert self.driver.current_url.__eq__("https://www.visitorcentre.hku.hk/")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def get_section_three(self):
        return self.driver.find_element(By.XPATH, "//div[@id='marketplace']")

    def get_visit_marketplace_option(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Visit Marketplace']")

    def click_visit_marketplace_option(self):
        self.get_visit_marketplace_option().click()

    def get_section_four(self):
        return self.driver.find_element(By.ID, "extension")

    def get_visit_all_option(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Visit All']")

    def click_visit_all_option(self):
        self.get_visit_all_option().click()

    def get_section_five(self):
        return self.driver.find_element(By.XPATH, "//div[@id='support']")

    def check_section_five_ui(self):
        element = self.driver.find_element(By.XPATH, "//div[@class='page-header']//div[@class='row']")
        assert element.value_of_css_property("padding-top").__eq__("10px")
        assert element.value_of_css_property("padding-bottom").__eq__("20px")
        assert element.value_of_css_property("text-align").__eq__("center")

    def get_section_six(self):
        return self.driver.find_element(By.XPATH, "//div[7]")

    def get_community_support_learn_more_option(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Learn More'][1]")

    def click_community_support_learn_more_option(self):
        self.get_community_support_learn_more_option().click()

    def check_community_forum_page(self):
        assert self.driver.title.__eq__("OpenCart Community - Index page")
        self.driver.back()

    def get_dedicated_support_learn_more_option(self):
        return self.driver.find_element(By.XPATH, "//*[@id='support']/div[2]/div[2]/p[2]/a[1]")

    def click_dedicated_support_learn_more_option(self):
        self.get_dedicated_support_learn_more_option().click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_dedicated_support_page(self):
        assert self.driver.title.__eq__("OpenCart Enterprise Services")

    def get_section_seven(self):
        return self.driver.find_element(By.ID, "press")

    def get_forbes_logo(self):
        return self.driver.find_element(By.XPATH, "//div[@id='press']/div[1]/div[1]/div[2]/ul/li/a/img")

    def click_forbes_logo(self):
        self.get_forbes_logo().click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_forbes_page(self):
        assert self.driver.title.__eq__("3 Steps To Launch Your First eCommerce Website")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def get_paypal_logo(self):
        return self.driver.find_element(By.XPATH, "//img[@title='PayPal']")

    def click_paypal_logo(self):
        self.get_paypal_logo().click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_paypal_page(self):
        assert self.driver.title.__eq__("PayPal for Business | Merchant Services | PayPal UK")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def get_bbc_logo(self):
        return self.driver.find_element(By.XPATH, "//div[@id='press']/div[1]/div[1]/div[2]/ul/li[3]/a/img")

    def click_bbc_logo(self):
        self.get_bbc_logo().click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_bbc_page(self):
        assert self.driver.title.__eq__("Tech tools make selling to the world child's play - BBC News")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def get_south_china_morning_post_logo(self):
        return self.driver.find_element(By.XPATH, "//div[@id='press']/div[1]/div[1]/div[2]/ul/li[4]/a/img")

    def click_south_china_morning_post_logo(self):
        self.get_south_china_morning_post_logo().click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_south_china_morning_post_page(self):
        assert self.driver.title.__eq__("A Business Mind: Daniel Kerr, founder of OpenCart | South China Morning Post")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def check_opencart_in_footer_options(self):
        assert self.driver.find_element(By.XPATH,"//div[@class='col-sm-2']").is_displayed()

    def click_feature_under_opencart(self):
        time.sleep(10)
        self.driver.find_element(By.XPATH, "//div[@class='row']/div[1]/section/ul/li/a").click()

    def click_showcase_under_opencart(self):
        self.driver.find_element(By.XPATH, "//div[@class='row']/div[1]/section/ul/li[2]/a").click()

    def check_resource_showcase_page(self):
        assert self.driver.title.__eq__("OpenCart - Showcase")

    def click_demo_under_opencart(self):
        self.driver.find_element(By.XPATH, "//div[@class='row']/div[1]/section/ul/li[3]/a").click()

    def click_download_under_opencart(self):
        self.driver.find_element(By.XPATH, "//div[@class='row']/div[1]/section/ul/li[4]/a").click()

    def click_marketplace_under_opencart(self):
        self.driver.find_element(By.XPATH,"//div[@class='row']/div[1]/section/ul/li[5]/a").click()

    def click_login_under_opencart(self):
        self.driver.find_element(By.XPATH, "//div[@class='row']/div[1]/section/ul/li[6]/a").click()

    def get_company_in_footer_options(self):
        return self.driver.find_element(By.XPATH,"//div[@class='row']//div[2]//section[1]")

    def click_contact_us_under_company(self):
        self.driver.find_element(By.XPATH, "//ul[@class='list-unstyled']//a[normalize-space()='Contact Us']").click()

    def check_contact_page(self):
        assert self.driver.title.__eq__("OpenCart - Contact")

    def click_extension_advertising_under_company(self):
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Extension Advertising']").click()

    def check_advertising_page(self):
        assert self.driver.title.__eq__("OpenCart - Advertising")

    def click_marketplace_advertising_under_company(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Marketplace Advertising']").click()

    def click_about_us_under_company(self):
        self.driver.find_element(By.XPATH,"//a[normalize-space()='About Us']").click()

    def check_company_page(self):
        assert self.driver.title.__eq__("OpenCart - Company")

    def click_terms_and_conditions_under_company(self):
        self.driver.find_element(By.XPATH,"//a[text()='Terms & Conditions']").click()

    def check_policy_page(self):
        assert self.driver.title.__eq__("OpenCart - Policy")

    def click_extension_developer_under_company(self):
        self.driver.find_element(By.XPATH,"//a[text()='Extension Developer']").click()

    def check_extension_developer_page(self):
        assert self.driver.title.__eq__("How to be a seller of Opencart?")

    def get_support_in_footer_options(self):
        return self.driver.find_element(By.XPATH, "//div[3]//section[1]")

    def click_community_forum_under_support(self):
        self.driver.find_element(By.LINK_TEXT, "Community Forum").click()

    def click_dedicated_support_under_support(self):
        self.driver.find_element(By.LINK_TEXT,"Dedicated Support").click()

    def check_support_page(self):
        self.driver.title.__eq__("OpenCart Enterprise Services")
        self.driver.back()

    def click_opencart_partners_under_support(self):
        self.driver.find_element(By.XPATH, "//ul[@class='list-unstyled']//a[text()='OpenCart Partners']").click()

    def check_resources_partners_page(self):
        assert self.driver.title.__eq__("OpenCart - Partners")

    def click_marketplace_support_under_support(self):
        self.driver.find_element(By.XPATH,"//ul[@class='list-unstyled']//a[text()='Marketplace Support']").click()

    def click_migrate_to_opencart_under_support(self):
        self.driver.find_element(By.XPATH, "//ul[@class='list-unstyled']//a[text()='Migrate to OpenCart']").click()

    def check_migrate_to_opencart_page(self):
        assert self.driver.title.__eq__("OpenCart - Cart2Cart Migration")

    def get_resources_in_footer_options(self):
        return self.driver.find_element(By.XPATH,"//div[4]//section[1]")

    def click_opencart_blog_under_resources(self):
        self.driver.find_element(By.LINK_TEXT,"OpenCart Blog").click()

    def click_opencart_documentation_under_resources(self):
        self.driver.find_element(By.XPATH,"//ul[@class='list-unstyled']//a[text()='OpenCart Documentation']").click()

    def check_resource_documentation_page(self):
        assert self.driver.title.__eq__("OpenCart Documentation")

    def click_opencart_books_under_resources(self):
        self.driver.find_element(By.XPATH,"//ul[@class='list-unstyled']//a[text()='OpenCart Books']").click()

    def check_resource_books_page(self):
        assert self.driver.title.__eq__("OpenCart Documentation")

    def click_github_bug_tracker_under_resources(self):
        self.driver.find_element(By.XPATH, "//body[1]/footer[1]/div[1]/div[1]/div[4]/section[1]/ul[1]/li[4]/a").click()

    def check_resources_github_bug_tracker_page(self):
        assert self.driver.current_url.__eq__("https://github.com/opencart/opencart/issues")
        self.driver.back()

    def click_developer_under_resources(self):
        self.driver.find_element(By.XPATH,"//ul[@class='list-unstyled']//a[text()='Developer']").click()

    def get_newsletter_in_footer_options(self):
        return self.driver.find_element(By.XPATH,"//section[@id='newsletter']")

    def check_newsletter_under_newsletter(self):
        words = self.driver.find_element(By.XPATH, "//section[@id='newsletter']//p").text
        assert words.__eq__("Subscribe to our newsletters and stay informed of new releases and other OpenCart events.")

    def check_placeholder_under_newsletter(self):
        assert self.driver.find_element(By.XPATH, "//section[@id='newsletter']//div/input").get_attribute(
            "placeholder")

    def get_social_section_under_newsletter(self):
        return self.driver.find_element(By.XPATH,"//div[@id='social']/ul")

    def click_facebook_marketing_partner_logo(self):
        self.driver.find_element(By.XPATH, "//div[@id='social']/ul/li/a/img").click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_meta_partners_page(self):
        assert self.driver.title.__eq__("Commerce | partner badge")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_linkedin_logo(self):
        self.driver.find_element(By.XPATH, "//div[@id='social']/ul/li[2]/a").click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_linkedin_page(self):
        assert self.driver.title.__eq__("LinkedIn Login, Sign in | LinkedIn")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_facebook_logo(self):
        self.driver.find_element(By.XPATH, "//div[@id='social']/ul/li[3]/a").click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_facebook_page(self):
        assert self.driver.current_url.__eq__("https://www.facebook.com/opencart/?ref=aymt_homepage_panel")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_twitter_logo(self):
        self.driver.find_element(By.XPATH, "//div[@id='social']/ul/li[4]/a").click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_twitter_page(self):
        assert self.driver.current_url.__eq__("https://twitter.com/opencart")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def enter_email_in_newsletter_field(self,email):
        self.driver.find_element(By.XPATH, "//section[@id='newsletter']/div/input").send_keys(email)

    def click_on_arrow_after_email(self):
        self.driver.find_element(By.XPATH, "//section[@id='newsletter']/div/div/button/i").click()
        time.sleep(5)

    def get_sign_up_newsletter_form(self):
        return self.driver.find_element(By.XPATH, "//div[@class='modal-content']")

    def check_footer_ui(self):
        element = self.driver.find_element(By.XPATH, "//body//footer")
        assert element.value_of_css_property("padding").__eq__("60px 0px")
        assert element.value_of_css_property("margin").__eq__("0px")
        assert element.value_of_css_property("font-size").__eq__("14px")
        assert element.value_of_css_property("line-height").__eq__("22.4px")