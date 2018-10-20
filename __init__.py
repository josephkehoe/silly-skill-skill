from mycroft import MycroftSkill, intent_file_handler


class SillySkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skill.silly.intent')
    def handle_skill_silly(self, message):
        self.speak_dialog('skill.silly')


def create_skill():
    return SillySkill()

