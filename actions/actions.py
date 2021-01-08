# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#
#         dispatcher.utter_message(text="One of Amar iSchool initiatives is to deliver advanced and effective education among students. We are an educational organization that provides high quality education to students through the provision of live videos produced by highly qualified teachers. We have been able to engage with students from 50 universities across Bangladesh since 2019.")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionAboutMe(Action):
    def name(self) -> Text:
        return "action_about_me"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="One of Amar iSchool initiatives is to deliver advanced and effective education among students. We are an educational organization that provides high quality education to students through the provision of live videos produced by highly qualified teachers. We have been able to engage with students from 50 universities across Bangladesh since 2019.")
        return []


class ActionAmariSchool(Action):
    def name(self) -> Text:
        return "action_about_Amar_iSchool"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="We provide quality and effective teaching to students by making and delivering various live videos on education through qualified teachers.")
        return []


class ActionTypeOfInstitution(Action):
    def name(self) -> Text:
        return "action_type_of_institution"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Sir, Amar iSchool is a platform for online learning.")
        return []


class ActionAboutService(Action):
    def name(self) -> Text:
        return "action_about_service"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="We're basically providing the XYZ service. Visit our website to learn more about our service.")
        return []


class ActionKindOfOrganization(Action):
    def name(self) -> Text:
        return "action_kind_of_organization"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Amar iSchool is a platform for online learning. Visit our website to learn more about our service.")
        return []


class ActionAboutWebsite(Action):
    def name(self) -> Text:
        return "action_about_website"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Yes sir/mam, could you please tell me which information is helpful for you?")
        return []

