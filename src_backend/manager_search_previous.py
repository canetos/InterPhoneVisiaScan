import logging

def set_manager_search_previous(self):
    logging.info("Lancement du programme de recherche précédent")
    #if face_recognition.current_name_index == 0:
    #    pass
    #else:
    #    face_recognition.current_name_index += 1
    label_name = "pyLbSerach_Hab"
    # Va chercher le nom précédent = ""
    #msg_name = update_name_display(self)
    #msg_name_hab = msg_name[0]
    #msg_number_app = msg_name[1]
    text_to_send = "Action en cours (précédente)"# f" Contacte : {msg_name_hab} \nNum appartement :\n{msg_number_app} "
    self.transmit_textonQML(text_to_send, label_name)