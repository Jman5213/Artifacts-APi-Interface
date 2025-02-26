import os
import dotenv
import requests
import json
import base64


dotenv.load_dotenv()


class Requests:
    def __init__(self, character):
        self.character = character
        self.token = os.getenv("TOKEN")
        self.base_url = "https://api.artifactsmmo.com"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}",
        }



    def __getattribute__(self, name):
        if name == "token":
            dotenv.load_dotenv()
            return os.getenv("TOKEN")
        else:
            return super().__getattribute__(name)


    def __get(self, endpoint:str) -> dict:
        """
        Takes the endpoint url, makes a GET request to the url with the data provided, and returns the response

        :param endpoint: A string representing the endpoint url
        :return: A dictionary representing the response
        """
        url = self.base_url + endpoint
        response = requests.get(url=url, headers=self.headers)
        return response.json()


    def __post(self, endpoint:str, data:dict=None) -> dict:
        """
       Takes the endpoint url, makes a POST request to the url with the data provided, and returns the response

       :param endpoint: A string representing the endpoint url
       :param data: A dictionary representing the data to be sent in the request
       :return: A dictionary representing the response
       """
        url = self.base_url + endpoint
        response = requests.post(url=url, data=json.dumps(data), headers=self.headers)
        return response.json()


    def __build_endpoint(self, task:str) -> str:
        """
        Takes task in format similar to the following:

        action fight
        action deposit
        info me
        info characters
        info bank
        token

        returns url endpoint for getting or posting to the artifacts api to complete the task

        :param task: A string representing the task
        :return: url endpoint for artifacts api to complete the task, or none if an error occurs due to index error
        """
        task.split()
        endpoints = {
            "info": {
                "me": "/characters/" + self.character.name,
                "bank": "/my/bank/items",
                "characters": "/my/characters"
            },
            "action": {
                "deposit": "/my/" + self.character.name + "/action/bank/deposit",
                "withdraw": "/my/" + self.character.name + "/action/bank/withdraw",
            }}

        try:
            if task[0] == "action" and task[1] not in ["deposit","withdraw"]:
                return "/my/"+self.character.name+"/action/"+task[1]
            elif task[0] == "token":
                return "/token"
            else:
                return endpoints[task[0]][task[1]]
        except IndexError:
            return "/"


    def request(self, task:str, data:dict=None) -> dict:
        """
        Makes post or get request based on task
        Uses data if a post request is made
        Returns the response

        :param task: A string representing the task
        :param data: A dictionary representing the data to be sent in the request
        :return: A dictionary representing the response
        """
        if "info" in task:
            return self.__get(endpoint=self.__build_endpoint(task))
        else:
            return self.__post(endpoint=self.__build_endpoint(task), data=data)



class Character:
    def __init__(self, name):
        self.name = name
        self.request = Requests(self)

        info = self.request.request("info me")

        self.name = info["name"]
        self.account = info["account"]
        self.skin = info["skin"]
        self.level = info["level"]
        self.xp = info["xp"]
        self.max_xp = info["max_xp"]
        self.gold = info["gold"]
        self.speed = info["speed"]
        self.mining_level = info["mining_level"]
        self.mining_xp = info["mining_xp"]
        self.mining_max_xp = info["mining_max_xp"]
        self.woodcutting_level = info["woodcutting_level"]
        self.woodcutting_xp = info["woodcutting_xp"]
        self.woodcutting_max_xp = info["woodcutting_max_xp"]
        self.fishing_level = info["fishing_level"]
        self.fishing_xp = info["fishing_xp"]
        self.fishing_max_xp = info["fishing_max_xp"]
        self.weaponcrafting_level = info["weaponcrafting_level"]
        self.weaponcrafting_xp = info["weaponcrafting_xp"]
        self.weaponcrafting_max_xp = info["weaponcrafting_max_xp"]
        self.gearcrafting_level = info["gearcrafting_level"]
        self.gearcrafting_xp = info["gearcrafting_xp"]
        self.gearcrafting_max_xp = info["gearcrafting_max_xp"]
        self.jewelrycrafting_level = info["jewelrycrafting_level"]
        self.jewelrycrafting_xp = info["jewelrycrafting_xp"]
        self.jewelrycrafting_max_xp = info["jewelrycrafting_max_xp"]
        self.cooking_level = info["cooking_level"]
        self.cooking_xp = info["cooking_xp"]
        self.cooking_max_xp = info["cooking_max_xp"]
        self.alchemy_level = info["alchemy_level"]
        self.alchemy_xp = info["alchemy_xp"]
        self.alchemy_max_xp = info["alchemy_max_xp"]
        self.hp = info["hp"]
        self.max_hp = info["max_hp"]
        self.haste = info["haste"]
        self.critical_strike = info["critical_strike"]
        self.wisdom = info["wisdom"]
        self.prospecting = info["prospecting"]
        self.attack_fire = info["attack_fire"]
        self.attack_earth = info["attack_earth"]
        self.attack_water = info["attack_water"]
        self.attack_air = info["attack_air"]
        self.dmg = info["dmg"]
        self.dmg_fire = info["dmg_fire"]
        self.dmg_earth = info["dmg_earth"]
        self.dmg_water = info["dmg_water"]
        self.dmg_air = info["dmg_air"]
        self.res_fire = info["res_fire"]
        self.res_earth = info["res_earth"]
        self.res_water = info["res_water"]
        self.res_air = info["res_air"]
        self.x = info["x"]
        self.y = info["y"]
        self.cooldown = info["cooldown"]
        self.cooldown_expiration = info["cooldown_expiration"]
        self.weapon_slot = info["weapon_slot"]
        self.rune_slot = info["rune_slot"]
        self.shield_slot = info["shield_slot"]
        self.helmet_slot = info["helmet_slot"]
        self.body_armor_slot = info["body_armor_slot"]
        self.leg_armor_slot = info["leg_armor_slot"]
        self.boots_slot = info["boots_slot"]
        self.ring1_slot = info["ring1_slot"]
        self.ring2_slot = info["ring2_slot"]
        self.amulet_slot = info["amulet_slot"]
        self.artifact1_slot = info["artifact1_slot"]
        self.artifact2_slot = info["artifact2_slot"]
        self.artifact3_slot = info["artifact3_slot"]
        self.utility1_slot = info["utility1_slot"]
        self.utility1_slot_quantity = info["utility1_slot_quantity"]
        self.utility2_slot = info["utility2_slot"]
        self.utility2_slot_quantity = info["utility2_slot_quantity"]
        self.bag_slot = ["bag_slot"]
        self.task = info["task"]
        self.task_type = info["task_type"]
        self.task_progress = info["task_progress"]
        self.task_total = info["task_total"]
        self.inventory_max_items = info["inventory_max_items"]
        self.inventory = info["inventory"]



    def move(self):
        self.request.request("",)


    def rest(self):
        self.request.request("",)


    def equip_item(self):
        self.request.request("",)


    def unequip_item(self):
        self.request.request("",)


    def use_item(self):
        self.request.request("",)


    def fight(self):
        self.request.request("",)


    def gather(self):
        self.request.request("",)


    def craft(self):
        self.request.request("",)


    def deposit(self):
        self.request.request("",)


    def withdraw(self):
        self.request.request("",)


    def recycle(self):
        self.request.request("",)


    def complete_task(self):
        self.request.request("",)


    def task_exchange(self):
        self.request.request("",)


    def accept_new_task(self):
        self.request.request("",)


    def __getattribute__(self, name):
        info = self.request.request("info me")

        self.name = info["name"]
        self.account = info["account"]
        self.skin = info["skin"]
        self.level = info["level"]
        self.xp = info["xp"]
        self.max_xp = info["max_xp"]
        self.gold = info["gold"]
        self.speed = info["speed"]
        self.mining_level = info["mining_level"]
        self.mining_xp = info["mining_xp"]
        self.mining_max_xp = info["mining_max_xp"]
        self.woodcutting_level = info["woodcutting_level"]
        self.woodcutting_xp = info["woodcutting_xp"]
        self.woodcutting_max_xp = info["woodcutting_max_xp"]
        self.fishing_level = info["fishing_level"]
        self.fishing_xp = info["fishing_xp"]
        self.fishing_max_xp = info["fishing_max_xp"]
        self.weaponcrafting_level = info["weaponcrafting_level"]
        self.weaponcrafting_xp = info["weaponcrafting_xp"]
        self.weaponcrafting_max_xp = info["weaponcrafting_max_xp"]
        self.gearcrafting_level = info["gearcrafting_level"]
        self.gearcrafting_xp = info["gearcrafting_xp"]
        self.gearcrafting_max_xp = info["gearcrafting_max_xp"]
        self.jewelrycrafting_level = info["jewelrycrafting_level"]
        self.jewelrycrafting_xp = info["jewelrycrafting_xp"]
        self.jewelrycrafting_max_xp = info["jewelrycrafting_max_xp"]
        self.cooking_level = info["cooking_level"]
        self.cooking_xp = info["cooking_xp"]
        self.cooking_max_xp = info["cooking_max_xp"]
        self.alchemy_level = info["alchemy_level"]
        self.alchemy_xp = info["alchemy_xp"]
        self.alchemy_max_xp = info["alchemy_max_xp"]
        self.hp = info["hp"]
        self.max_hp = info["max_hp"]
        self.haste = info["haste"]
        self.critical_strike = info["critical_strike"]
        self.wisdom = info["wisdom"]
        self.prospecting = info["prospecting"]
        self.attack_fire = info["attack_fire"]
        self.attack_earth = info["attack_earth"]
        self.attack_water = info["attack_water"]
        self.attack_air = info["attack_air"]
        self.dmg = info["dmg"]
        self.dmg_fire = info["dmg_fire"]
        self.dmg_earth = info["dmg_earth"]
        self.dmg_water = info["dmg_water"]
        self.dmg_air = info["dmg_air"]
        self.res_fire = info["res_fire"]
        self.res_earth = info["res_earth"]
        self.res_water = info["res_water"]
        self.res_air = info["res_air"]
        self.x = info["x"]
        self.y = info["y"]
        self.cooldown = info["cooldown"]
        self.cooldown_expiration = info["cooldown_expiration"]
        self.weapon_slot = info["weapon_slot"]
        self.rune_slot = info["rune_slot"]
        self.shield_slot = info["shield_slot"]
        self.helmet_slot = info["helmet_slot"]
        self.body_armor_slot = info["body_armor_slot"]
        self.leg_armor_slot = info["leg_armor_slot"]
        self.boots_slot = info["boots_slot"]
        self.ring1_slot = info["ring1_slot"]
        self.ring2_slot = info["ring2_slot"]
        self.amulet_slot = info["amulet_slot"]
        self.artifact1_slot = info["artifact1_slot"]
        self.artifact2_slot = info["artifact2_slot"]
        self.artifact3_slot = info["artifact3_slot"]
        self.utility1_slot = info["utility1_slot"]
        self.utility1_slot_quantity = info["utility1_slot_quantity"]
        self.utility2_slot = info["utility2_slot"]
        self.utility2_slot_quantity = info["utility2_slot_quantity"]
        self.bag_slot = ["bag_slot"]
        self.task = info["task"]
        self.task_type = info["task_type"]
        self.task_progress = info["task_progress"]
        self.task_total = info["task_total"]
        self.inventory_max_items = info["inventory_max_items"]
        self.inventory = info["inventory"]

        return super().__getattribute__(name)


class Account:
    def __init__(self, username, password):
        #login, get new token
        self.auth = str(username+":"+password).encode("utf-8")
        base64.b64encode(self.auth).decode("utf-8")

        dotenv.load_dotenv()
        dotenv.set_key("variables.env","TOKEN",self.auth)
        self.request = Requests(self)
        token = self.request.request("token")
        dotenv.set_key("variables.env","TOKEN",token["token"])

        self.characters = []
        for character in self.request.request("info characters"):
            self.characters.append(Character(character["name"]))
        ...