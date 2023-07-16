from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSayUserName(Action):

    def name(self) -> Text:
        return "action_say_user_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_name = tracker.get_slot('user_name')
        if not user_name:
            dispatcher.utter_message(text='Я не знаю твоего имени:(')
        else:
            dispatcher.utter_message(text=f'Твое имя: {user_name}')
        return []
