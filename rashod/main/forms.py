from django import forms
from .models import Kursy, bolnyes, naryads, uvolnenies, otpusks

class KursyModelForm(forms.ModelForm):
    class Meta:
        model = Kursy
        fields = ['poSpisku', 'naLitso', 'naryad','bolnye','uvolnenie','otpusk']



class PoSpiskuForm(forms.ModelForm):
    class Meta:
        model = Kursy
        fields = ['poSpisku']
        labels = {
            'poSpisku': '',
        }

class NaLitsoForm(forms.ModelForm):
    class Meta:
        model = Kursy
        fields = ['naLitso']
        labels = {
            'naLitso': '',
        }

class NaryadForm(forms.ModelForm):
    class Meta:
        model = Kursy
        fields = ['naryad']
        labels = {
            'naryad': '',
        }

class BolnyeForm(forms.ModelForm):
    class Meta:
        model = Kursy
        fields = ['bolnye']
        labels = {
            'bolnye': '',
        }

class UvolnenieForm(forms.ModelForm):
    class Meta:
        model = Kursy
        fields = ['uvolnenie']
        labels = {
            'uvolnenie': '',
        }

class OtpuskForm(forms.ModelForm):
    class Meta:
        model = Kursy
        fields = ['otpusk']
        labels = {
            'otpusk': '',
        }



class bolnyesModelForm(forms.ModelForm):
    class Meta:
        model = bolnyes
        fields = ['information_of_bolnyes','information_of_bolnyes_2','information_of_bolnyes_3','information_of_bolnyes_4',
                    'information_of_bolnyes_5','information_of_bolnyes_6','information_of_bolnyes_7','information_of_bolnyes_8',
                    'information_of_bolnyes_9','information_of_bolnyes_10','information_of_bolnyes_11','information_of_bolnyes_12',
                    'information_of_bolnyes_13','information_of_bolnyes_14','information_of_bolnyes_15','information_of_bolnyes_16',
                    'information_of_bolnyes_17','information_of_bolnyes_18','information_of_bolnyes_19','information_of_bolnyes_20'
                    ,'information_of_bolnyes_21','information_of_bolnyes_22','information_of_bolnyes_23','information_of_bolnyes_24'
                    ,'information_of_bolnyes_25','information_of_bolnyes_26','information_of_bolnyes_27','information_of_bolnyes_28'
                    ,'information_of_bolnyes_29','information_of_bolnyes_30','information_of_bolnyes_31','information_of_bolnyes_32'
                    ,'information_of_bolnyes_33','information_of_bolnyes_34','information_of_bolnyes_35','information_of_bolnyes_36'
                    ,'information_of_bolnyes_37','information_of_bolnyes_38','information_of_bolnyes_39','information_of_bolnyes_40']
        labels = {
            'information_of_bolnyes': ' 1','information_of_bolnyes_2': ' 2','information_of_bolnyes_3': ' 3','information_of_bolnyes_4': ' 4',
                    'information_of_bolnyes_5': ' 5','information_of_bolnyes_6': ' 6','information_of_bolnyes_7': ' 7','information_of_bolnyes_8': ' 8',
                    'information_of_bolnyes_9': ' 9','information_of_bolnyes_10': '10','information_of_bolnyes_11': '11','information_of_bolnyes_12': '12',
                    'information_of_bolnyes_13': '13','information_of_bolnyes_14': '14','information_of_bolnyes_15': '15','information_of_bolnyes_16': '16',
                    'information_of_bolnyes_17': '17','information_of_bolnyes_18': '18','information_of_bolnyes_19': '19','information_of_bolnyes_20': '20'
                    ,'information_of_bolnyes_21': '21','information_of_bolnyes_22': '22','information_of_bolnyes_23': '23','information_of_bolnyes_24': '24'
                    ,'information_of_bolnyes_25': '25','information_of_bolnyes_26': '26','information_of_bolnyes_27': '27','information_of_bolnyes_28': '28'
                    ,'information_of_bolnyes_29': '29','information_of_bolnyes_30': '30','information_of_bolnyes_31': '31','information_of_bolnyes_32': '32'
                    ,'information_of_bolnyes_33': '33','information_of_bolnyes_34': '34','information_of_bolnyes_35': '35','information_of_bolnyes_36': '36'
                    ,'information_of_bolnyes_37': '37','information_of_bolnyes_38': '38','information_of_bolnyes_39': '39','information_of_bolnyes_40': '40'
        }

class naryadsModelForm(forms.ModelForm):
    class Meta:
        model = naryads
        fields = ['information_of_naryads','information_of_naryads_2','information_of_naryads_3','information_of_naryads_4'
                    ,'information_of_naryads_5','information_of_naryads_6','information_of_naryads_7','information_of_naryads_8'
                    ,'information_of_naryads_9','information_of_naryads_10','information_of_naryads_11','information_of_naryads_12'
                    ,'information_of_naryads_13','information_of_naryads_14','information_of_naryads_15','information_of_naryads_16'
                    ,'information_of_naryads_17','information_of_naryads_18','information_of_naryads_19','information_of_naryads_20'
                    ,'information_of_naryads_21','information_of_naryads_22','information_of_naryads_23','information_of_naryads_24'
                    ,'information_of_naryads_25','information_of_naryads_26','information_of_naryads_27','information_of_naryads_28'
                    ,'information_of_naryads_29','information_of_naryads_30','information_of_naryads_31','information_of_naryads_32'
                    ,'information_of_naryads_33','information_of_naryads_34','information_of_naryads_35','information_of_naryads_36'
                    ,'information_of_naryads_37','information_of_naryads_38','information_of_naryads_39','information_of_naryads_40']
        labels = { 'information_of_naryads': '1','information_of_naryads_2': '2','information_of_naryads_3': '3','information_of_naryads_4': '4'
                    ,'information_of_naryads_5': '5','information_of_naryads_6': '6','information_of_naryads_7': '7','information_of_naryads_8': '8'
                    ,'information_of_naryads_9': '9','information_of_naryads_10': '10','information_of_naryads_11': '11','information_of_naryads_12': '12'
                    ,'information_of_naryads_13': '13','information_of_naryads_14': '14','information_of_naryads_15': '15','information_of_naryads_16': '16'
                    ,'information_of_naryads_17': '17','information_of_naryads_18': '18','information_of_naryads_19': '19','information_of_naryads_20': '20'
                    ,'information_of_naryads_21': '21','information_of_naryads_22': '22','information_of_naryads_23': '23','information_of_naryads_24': '24'
                    ,'information_of_naryads_25': '25','information_of_naryads_26': '26','information_of_naryads_27': '27','information_of_naryads_28': '28'
                    ,'information_of_naryads_29': '29','information_of_naryads_30': '30','information_of_naryads_31': '31','information_of_naryads_32': '32'
                    ,'information_of_naryads_33': '33','information_of_naryads_34': '34','information_of_naryads_35': '35','information_of_naryads_36': '36'
                    ,'information_of_naryads_37': '37','information_of_naryads_38': '38','information_of_naryads_39': '39','information_of_naryads_40': '40'

        }

class uvolneniesModelForm(forms.ModelForm):
    class Meta:
        model = uvolnenies
        fields = ['information_of_uvolnenies','information_of_uvolnenies_2','information_of_uvolnenies_3','information_of_uvolnenies_4'
                    ,'information_of_uvolnenies_5','information_of_uvolnenies_6','information_of_uvolnenies_7','information_of_uvolnenies_8'
                    ,'information_of_uvolnenies_9','information_of_uvolnenies_10','information_of_uvolnenies_11','information_of_uvolnenies_12'
                    ,'information_of_uvolnenies_13','information_of_uvolnenies_14','information_of_uvolnenies_15','information_of_uvolnenies_16'
                    ,'information_of_uvolnenies_17','information_of_uvolnenies_18','information_of_uvolnenies_19','information_of_uvolnenies_20'
                    ,'information_of_uvolnenies_21','information_of_uvolnenies_22','information_of_uvolnenies_23','information_of_uvolnenies_24'
                    ,'information_of_uvolnenies_25','information_of_uvolnenies_26','information_of_uvolnenies_27','information_of_uvolnenies_28'
                    ,'information_of_uvolnenies_29','information_of_uvolnenies_30','information_of_uvolnenies_31','information_of_uvolnenies_32'
                    ,'information_of_uvolnenies_33','information_of_uvolnenies_34','information_of_uvolnenies_35','information_of_uvolnenies_36'
                    ,'information_of_uvolnenies_37','information_of_uvolnenies_38','information_of_uvolnenies_39','information_of_uvolnenies_40']
        labels = {'information_of_uvolnenies': '1','information_of_uvolnenies_2': '2','information_of_uvolnenies_3': '3','information_of_uvolnenies_4': '4'
                    ,'information_of_uvolnenies_5': '5','information_of_uvolnenies_6': '6','information_of_uvolnenies_7': '7','information_of_uvolnenies_8': '8'
                    ,'information_of_uvolnenies_9': '9','information_of_uvolnenies_10': '10','information_of_uvolnenies_11': '11','information_of_uvolnenies_12': '12'
                    ,'information_of_uvolnenies_13': '13','information_of_uvolnenies_14': '14','information_of_uvolnenies_15': '15','information_of_uvolnenies_16': '16'
                    ,'information_of_uvolnenies_17': '17','information_of_uvolnenies_18': '18','information_of_uvolnenies_19': '19','information_of_uvolnenies_20': '20'
                    ,'information_of_uvolnenies_21': '21','information_of_uvolnenies_22': '22','information_of_uvolnenies_23': '23','information_of_uvolnenies_24': '24'
                    ,'information_of_uvolnenies_25': '25','information_of_uvolnenies_26': '26','information_of_uvolnenies_27': '27','information_of_uvolnenies_28': '28'
                    ,'information_of_uvolnenies_29': '29','information_of_uvolnenies_30': '30','information_of_uvolnenies_31': '31','information_of_uvolnenies_32': '32'
                    ,'information_of_uvolnenies_33': '33','information_of_uvolnenies_34': '34','information_of_uvolnenies_35': '35','information_of_uvolnenies_36': '36'
                    ,'information_of_uvolnenies_37': '37','information_of_uvolnenies_38': '38','information_of_uvolnenies_39': '39','information_of_uvolnenies_40': '40'
        }


class otpusksModelForm(forms.ModelForm):
    class Meta:
        model = otpusks
        fields = ['information_of_otpusks','information_of_otpusks_2','information_of_otpusks_3','information_of_otpusks_4'
                    ,'information_of_otpusks_5','information_of_otpusks_6','information_of_otpusks_7','information_of_otpusks_8'
                    ,'information_of_otpusks_9','information_of_otpusks_10','information_of_otpusks_11','information_of_otpusks_12'
                    ,'information_of_otpusks_13','information_of_otpusks_14','information_of_otpusks_15','information_of_otpusks_16'
                    ,'information_of_otpusks_17','information_of_otpusks_18','information_of_otpusks_19','information_of_otpusks_20'
                    ,'information_of_otpusks_21','information_of_otpusks_22','information_of_otpusks_23','information_of_otpusks_24'
                    ,'information_of_otpusks_25','information_of_otpusks_26','information_of_otpusks_27','information_of_otpusks_28'
                    ,'information_of_otpusks_29','information_of_otpusks_30','information_of_otpusks_31','information_of_otpusks_32'
                    ,'information_of_otpusks_33','information_of_otpusks_34','information_of_otpusks_35','information_of_otpusks_36'
                    ,'information_of_otpusks_37','information_of_otpusks_38','information_of_otpusks_39','information_of_otpusks_40']
        labels = {'information_of_otpusks': '1','information_of_otpusks_2': '2','information_of_otpusks_3': '3','information_of_otpusks_4': '4'
                    ,'information_of_otpusks_5': '5','information_of_otpusks_6': '6','information_of_otpusks_7': '7','information_of_otpusks_8': '8'
                    ,'information_of_otpusks_9': '9','information_of_otpusks_10': '10','information_of_otpusks_11': '11','information_of_otpusks_12': '12'
                    ,'information_of_otpusks_13': '13','information_of_otpusks_14': '14','information_of_otpusks_15': '15','information_of_otpusks_16': '16'
                    ,'information_of_otpusks_17': '17','information_of_otpusks_18': '18','information_of_otpusks_19': '19','information_of_otpusks_20': '20'
                    ,'information_of_otpusks_21': '21','information_of_otpusks_22': '22','information_of_otpusks_23': '23','information_of_otpusks_24': '24'
                    ,'information_of_otpusks_25': '25','information_of_otpusks_26': '26','information_of_otpusks_27': '27','information_of_otpusks_28': '28'
                    ,'information_of_otpusks_29': '29','information_of_otpusks_30': '30','information_of_otpusks_31': '31','information_of_otpusks_32': '32'
                    ,'information_of_otpusks_33': '33','information_of_otpusks_34': '34','information_of_otpusks_35': '35','information_of_otpusks_36': '36'
                    ,'information_of_otpusks_37': '37','information_of_otpusks_38': '38','information_of_otpusks_39': '39','information_of_otpusks_40': '40'

        }