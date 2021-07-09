#coding:utf-8



class Main_manage():
    pass

    def left_menu_click(self, menu, second_menu):
        """点击左侧大菜单"""
        self._params["menu"] = menu
        self._params["second_menu"] = second_menu
        self.sleep(1)
        _new_data = self.replace_yaml_variable(_data, self._params)
        menu_element = yamlstr_to_tuple(_new_data["menu_element"])
        second_menu_element = yamlstr_to_tuple(_new_data["second_menu_element"])
        # menu_element = (By.XPATH,"//span[contains(text(),'%s')]"%menu)
        self.click(menu_element)
        self.sleep(1)
        return self.__left_second_menu_click(second_menu_element)

    def __left_second_menu_click(self, second_menu):
        """点击第二级菜单"""
        # self._params["second_menu"] = second_menu
        self.sleep(1)
        # second_menu_element = (By.XPATH, "//li[contains(text(),'%s')]" % second_menu)
        # _new_data = self.replace_yaml_variable(_data, self._params)
        # second_menu_element = yamlstr_to_tuple(_new_data["second_menu_element"])
        self.click(second_menu)
        self.sleep(1)
        # if second_menu=="商户管理":
        #     return MerchantManage(self.driver)
        # elif second_menu=="产品管理":
        #     return ProductManage(self.driver)
        # elif second_menu=="用户管理":
        #     return UserManage(self.driver)
