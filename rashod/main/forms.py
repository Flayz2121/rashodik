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





#Больные++
class bolnyesModelForm(forms.ModelForm):
    class Meta:
        model = bolnyes
        fields = ['information_of_bolnyes_1','information_of_bolnyes_2','information_of_bolnyes_3','information_of_bolnyes_4',
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
            'information_of_bolnyes_1': ' 1','information_of_bolnyes_2': ' 2','information_of_bolnyes_3': ' 3','information_of_bolnyes_4': ' 4',
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

class bolnyesMestoModelForm(forms.ModelForm):
    class Meta:
        model = bolnyes
        fields = ['info_of_bolnyes_1_mesto','info_of_bolnyes_2_mesto','info_of_bolnyes_3_mesto','info_of_bolnyes_4_mesto',
                    'info_of_bolnyes_5_mesto','info_of_bolnyes_6_mesto','info_of_bolnyes_7_mesto','info_of_bolnyes_8_mesto',
                    'info_of_bolnyes_9_mesto','info_of_bolnyes_10_mesto','info_of_bolnyes_11_mesto','info_of_bolnyes_12_mesto',
                    'info_of_bolnyes_13_mesto','info_of_bolnyes_14_mesto','info_of_bolnyes_15_mesto','info_of_bolnyes_16_mesto',
                    'info_of_bolnyes_17_mesto','info_of_bolnyes_18_mesto','info_of_bolnyes_19_mesto','info_of_bolnyes_20_mesto'
                    ,'info_of_bolnyes_21_mesto','info_of_bolnyes_22_mesto','info_of_bolnyes_23_mesto','info_of_bolnyes_24_mesto'
                    ,'info_of_bolnyes_25_mesto','info_of_bolnyes_26_mesto','info_of_bolnyes_27_mesto','info_of_bolnyes_28_mesto'
                    ,'info_of_bolnyes_29_mesto','info_of_bolnyes_30_mesto','info_of_bolnyes_31_mesto','info_of_bolnyes_32_mesto'
                    ,'info_of_bolnyes_33_mesto','info_of_bolnyes_34_mesto','info_of_bolnyes_35_mesto','info_of_bolnyes_36_mesto'
                    ,'info_of_bolnyes_37_mesto','info_of_bolnyes_38_mesto','info_of_bolnyes_39_mesto','info_of_bolnyes_40_mesto']
        labels = {
            'info_of_bolnyes_1_mesto': '','info_of_bolnyes_2_mesto': '','info_of_bolnyes_3_mesto': '','info_of_bolnyes_4_mesto': '',
                    'info_of_bolnyes_5_mesto': '','info_of_bolnyes_6_mesto': '','info_of_bolnyes_7_mesto': '','info_of_bolnyes_8_mesto': '',
                    'info_of_bolnyes_9_mesto': '','info_of_bolnyes_10_mesto': '','info_of_bolnyes_11_mesto': '','info_of_bolnyes_12_mesto': '',
                    'info_of_bolnyes_13_mesto': '','info_of_bolnyes_14_mesto': '','info_of_bolnyes_15_mesto': '','info_of_bolnyes_16_mesto': '',
                    'info_of_bolnyes_17_mesto': '','info_of_bolnyes_18_mesto': '','info_of_bolnyes_19_mesto': '','info_of_bolnyes_20_mesto': ''
                    ,'info_of_bolnyes_21_mesto': '','info_of_bolnyes_22_mesto': '','info_of_bolnyes_23_mesto': '','info_of_bolnyes_24_mesto': ''
                    ,'info_of_bolnyes_25_mesto': '','info_of_bolnyes_26_mesto': '','info_of_bolnyes_27_mesto': '','info_of_bolnyes_28_mesto': ''
                    ,'info_of_bolnyes_29_mesto': '','info_of_bolnyes_30_mesto': '','info_of_bolnyes_31_mesto': '','info_of_bolnyes_32_mesto': ''
                    ,'info_of_bolnyes_33_mesto': '','info_of_bolnyes_34_mesto': '','info_of_bolnyes_35_mesto': '','info_of_bolnyes_36_mesto': ''
                    ,'info_of_bolnyes_37_mesto': '','info_of_bolnyes_38_mesto': '','info_of_bolnyes_39_mesto': '','info_of_bolnyes_40_mesto': ''
        }

class bolnyesVremyaModelForm(forms.ModelForm):
    class Meta:
        model = bolnyes
        fields = ['info_of_bolnyes_1_vremya','info_of_bolnyes_2_vremya','info_of_bolnyes_3_vremya','info_of_bolnyes_4_vremya',
                    'info_of_bolnyes_5_vremya','info_of_bolnyes_6_vremya','info_of_bolnyes_7_vremya','info_of_bolnyes_8_vremya',
                    'info_of_bolnyes_9_vremya','info_of_bolnyes_10_vremya','info_of_bolnyes_11_vremya','info_of_bolnyes_12_vremya',
                    'info_of_bolnyes_13_vremya','info_of_bolnyes_14_vremya','info_of_bolnyes_15_vremya','info_of_bolnyes_16_vremya',
                    'info_of_bolnyes_17_vremya','info_of_bolnyes_18_vremya','info_of_bolnyes_19_vremya','info_of_bolnyes_20_vremya'
                    ,'info_of_bolnyes_21_vremya','info_of_bolnyes_22_vremya','info_of_bolnyes_23_vremya','info_of_bolnyes_24_vremya'
                    ,'info_of_bolnyes_25_vremya','info_of_bolnyes_26_vremya','info_of_bolnyes_27_vremya','info_of_bolnyes_28_vremya'
                    ,'info_of_bolnyes_29_vremya','info_of_bolnyes_30_vremya','info_of_bolnyes_31_vremya','info_of_bolnyes_32_vremya'
                    ,'info_of_bolnyes_33_vremya','info_of_bolnyes_34_vremya','info_of_bolnyes_35_vremya','info_of_bolnyes_36_vremya'
                    ,'info_of_bolnyes_37_vremya','info_of_bolnyes_38_vremya','info_of_bolnyes_39_vremya','info_of_bolnyes_40_vremya']
        labels = {
            'info_of_bolnyes_1_vremya': '','info_of_bolnyes_2_vremya': '','info_of_bolnyes_3_vremya': '','info_of_bolnyes_4_vremya': '',
                    'info_of_bolnyes_5_vremya': '','info_of_bolnyes_6_vremya': '','info_of_bolnyes_7_vremya': '','info_of_bolnyes_8_vremya': '',
                    'info_of_bolnyes_9_vremya': '','info_of_bolnyes_10_vremya': '','info_of_bolnyes_11_vremya': '','info_of_bolnyes_12_vremya': '',
                    'info_of_bolnyes_13_vremya': '','info_of_bolnyes_14_vremya': '','info_of_bolnyes_15_vremya': '','info_of_bolnyes_16_vremya': '',
                    'info_of_bolnyes_17_vremya': '','info_of_bolnyes_18_vremya': '','info_of_bolnyes_19_vremya': '','info_of_bolnyes_20_vremya': ''
                    ,'info_of_bolnyes_21_vremya': '','info_of_bolnyes_22_vremya': '','info_of_bolnyes_23_vremya': '','info_of_bolnyes_24_vremya': ''
                    ,'info_of_bolnyes_25_vremya': '','info_of_bolnyes_26_vremya': '','info_of_bolnyes_27_vremya': '','info_of_bolnyes_28_vremya': ''
                    ,'info_of_bolnyes_29_vremya': '','info_of_bolnyes_30_vremya': '','info_of_bolnyes_31_vremya': '','info_of_bolnyes_32_vremya': ''
                    ,'info_of_bolnyes_33_vremya': '','info_of_bolnyes_34_vremya': '','info_of_bolnyes_35_vremya': '','info_of_bolnyes_36_vremya': ''
                    ,'info_of_bolnyes_37_vremya': '','info_of_bolnyes_38_vremya': '','info_of_bolnyes_39_vremya': '','info_of_bolnyes_40_vremya': ''
        }











#Наряд++
class naryadsModelForm(forms.ModelForm):
    class Meta:
        model = naryads
        fields = ['information_of_naryads_1','information_of_naryads_2','information_of_naryads_3','information_of_naryads_4'
                    ,'information_of_naryads_5','information_of_naryads_6','information_of_naryads_7','information_of_naryads_8'
                    ,'information_of_naryads_9','information_of_naryads_10','information_of_naryads_11','information_of_naryads_12'
                    ,'information_of_naryads_13','information_of_naryads_14','information_of_naryads_15','information_of_naryads_16'
                    ,'information_of_naryads_17','information_of_naryads_18','information_of_naryads_19','information_of_naryads_20'
                    ,'information_of_naryads_21','information_of_naryads_22','information_of_naryads_23','information_of_naryads_24'
                    ,'information_of_naryads_25','information_of_naryads_26','information_of_naryads_27','information_of_naryads_28'
                    ,'information_of_naryads_29','information_of_naryads_30','information_of_naryads_31','information_of_naryads_32'
                    ,'information_of_naryads_33','information_of_naryads_34','information_of_naryads_35','information_of_naryads_36'
                    ,'information_of_naryads_37','information_of_naryads_38','information_of_naryads_39','information_of_naryads_40']
        labels = { 'information_of_naryads_1': '1','information_of_naryads_2': '2','information_of_naryads_3': '3','information_of_naryads_4': '4'
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

class naryadsMestoModelForm(forms.ModelForm):
    class Meta:
        model = naryads
        fields = ['info_of_naryads_1_mesto','info_of_naryads_2_mesto','info_of_naryads_3_mesto','info_of_naryads_4_mesto'
                    ,'info_of_naryads_5_mesto','info_of_naryads_6_mesto','info_of_naryads_7_mesto','info_of_naryads_8_mesto'
                    ,'info_of_naryads_9_mesto','info_of_naryads_10_mesto','info_of_naryads_11_mesto','info_of_naryads_12_mesto'
                    ,'info_of_naryads_13_mesto','info_of_naryads_14_mesto','info_of_naryads_15_mesto','info_of_naryads_16_mesto'
                    ,'info_of_naryads_17_mesto','info_of_naryads_18_mesto','info_of_naryads_19_mesto','info_of_naryads_20_mesto'
                    ,'info_of_naryads_21_mesto','info_of_naryads_22_mesto','info_of_naryads_23_mesto','info_of_naryads_24_mesto'
                    ,'info_of_naryads_25_mesto','info_of_naryads_26_mesto','info_of_naryads_27_mesto','info_of_naryads_28_mesto'
                    ,'info_of_naryads_29_mesto','info_of_naryads_30_mesto','info_of_naryads_31_mesto','info_of_naryads_32_mesto'
                    ,'info_of_naryads_33_mesto','info_of_naryads_34_mesto','info_of_naryads_35_mesto','info_of_naryads_36_mesto'
                    ,'info_of_naryads_37_mesto','info_of_naryads_38_mesto','info_of_naryads_39_mesto','info_of_naryads_40_mesto']
        labels = { 'info_of_naryads_1_mesto': '','info_of_naryads_2_mesto': '','info_of_naryads_3_mesto': '','info_of_naryads_4_mesto': ''
                    ,'info_of_naryads_5_mesto': '','info_of_naryads_6_mesto': '','info_of_naryads_7_mesto': '','info_of_naryads_8_mesto': ''
                    ,'info_of_naryads_9_mesto': '','info_of_naryads_10_mesto': '','info_of_naryads_11_mesto': '','info_of_naryads_12_mesto': ''
                    ,'info_of_naryads_13_mesto': '','info_of_naryads_14_mesto': '','info_of_naryads_15_mesto': '','info_of_naryads_16_mesto': ''
                    ,'info_of_naryads_17_mesto': '','info_of_naryads_18_mesto': '','info_of_naryads_19_mesto': '','info_of_naryads_20_mesto': ''
                    ,'info_of_naryads_21_mesto': '','info_of_naryads_22_mesto': '','info_of_naryads_23_mesto': '','info_of_naryads_24_mesto': ''
                    ,'info_of_naryads_25_mesto': '','info_of_naryads_26_mesto': '','info_of_naryads_27_mesto': '','info_of_naryads_28_mesto': ''
                    ,'info_of_naryads_29_mesto': '','info_of_naryads_30_mesto': '','info_of_naryads_31_mesto': '','info_of_naryads_32_mesto': ''
                    ,'info_of_naryads_33_mesto': '','info_of_naryads_34_mesto': '','info_of_naryads_35_mesto': '','info_of_naryads_36_mesto': ''
                    ,'info_of_naryads_37_mesto': '','info_of_naryads_38_mesto': '','info_of_naryads_39_mesto': '','info_of_naryads_40_mesto': ''
        }

class naryadsVremyaModelForm(forms.ModelForm):
    class Meta:
        model = naryads
        fields = ['info_of_naryads_1_vremya','info_of_naryads_2_vremya','info_of_naryads_3_vremya','info_of_naryads_4_vremya'
                    ,'info_of_naryads_5_vremya','info_of_naryads_6_vremya','info_of_naryads_7_vremya','info_of_naryads_8_vremya'
                    ,'info_of_naryads_9_vremya','info_of_naryads_10_vremya','info_of_naryads_11_vremya','info_of_naryads_12_vremya'
                    ,'info_of_naryads_13_vremya','info_of_naryads_14_vremya','info_of_naryads_15_vremya','info_of_naryads_16_vremya'
                    ,'info_of_naryads_17_vremya','info_of_naryads_18_vremya','info_of_naryads_19_vremya','info_of_naryads_20_vremya'
                    ,'info_of_naryads_21_vremya','info_of_naryads_22_vremya','info_of_naryads_23_vremya','info_of_naryads_24_vremya'
                    ,'info_of_naryads_25_vremya','info_of_naryads_26_vremya','info_of_naryads_27_vremya','info_of_naryads_28_vremya'
                    ,'info_of_naryads_29_vremya','info_of_naryads_30_vremya','info_of_naryads_31_vremya','info_of_naryads_32_vremya'
                    ,'info_of_naryads_33_vremya','info_of_naryads_34_vremya','info_of_naryads_35_vremya','info_of_naryads_36_vremya'
                    ,'info_of_naryads_37_vremya','info_of_naryads_38_vremya','info_of_naryads_39_vremya','info_of_naryads_40_vremya']
        labels = { 'info_of_naryads_1_vremya': '','info_of_naryads_2_vremya': '','info_of_naryads_3_vremya': '','info_of_naryads_4_vremya': ''
                    ,'info_of_naryads_5_vremya': '','info_of_naryads_6_vremya': '','info_of_naryads_7_vremya': '','info_of_naryads_8_vremya': ''
                    ,'info_of_naryads_9_vremya': '','info_of_naryads_10_vremya': '','info_of_naryads_11_vremya': '','info_of_naryads_12_vremya': ''
                    ,'info_of_naryads_13_vremya': '','info_of_naryads_14_vremya': '','info_of_naryads_15_vremya': '','info_of_naryads_16_vremya': ''
                    ,'info_of_naryads_17_vremya': '','info_of_naryads_18_vremya': '','info_of_naryads_19_vremya': '','info_of_naryads_20_vremya': ''
                    ,'info_of_naryads_21_vremya': '','info_of_naryads_22_vremya': '','info_of_naryads_23_vremya': '','info_of_naryads_24_vremya': ''
                    ,'info_of_naryads_25_vremya': '','info_of_naryads_26_vremya': '','info_of_naryads_27_vremya': '','info_of_naryads_28_vremya': ''
                    ,'info_of_naryads_29_vremya': '','info_of_naryads_30_vremya': '','info_of_naryads_31_vremya': '','info_of_naryads_32_vremya': ''
                    ,'info_of_naryads_33_vremya': '','info_of_naryads_34_vremya': '','info_of_naryads_35_vremya': '','info_of_naryads_36_vremya': ''
                    ,'info_of_naryads_37_vremya': '','info_of_naryads_38_vremya': '','info_of_naryads_39_vremya': '','info_of_naryads_40_vremya': ''
        }









#Уывольнения--
class uvolneniesModelForm(forms.ModelForm):
    class Meta:
        model = uvolnenies
        fields = ['information_of_uvolnenies_1','information_of_uvolnenies_2','information_of_uvolnenies_3','information_of_uvolnenies_4'
                    ,'information_of_uvolnenies_5','information_of_uvolnenies_6','information_of_uvolnenies_7','information_of_uvolnenies_8'
                    ,'information_of_uvolnenies_9','information_of_uvolnenies_10','information_of_uvolnenies_11','information_of_uvolnenies_12'
                    ,'information_of_uvolnenies_13','information_of_uvolnenies_14','information_of_uvolnenies_15','information_of_uvolnenies_16'
                    ,'information_of_uvolnenies_17','information_of_uvolnenies_18','information_of_uvolnenies_19','information_of_uvolnenies_20'
                    ,'information_of_uvolnenies_21','information_of_uvolnenies_22','information_of_uvolnenies_23','information_of_uvolnenies_24'
                    ,'information_of_uvolnenies_25','information_of_uvolnenies_26','information_of_uvolnenies_27','information_of_uvolnenies_28'
                    ,'information_of_uvolnenies_29','information_of_uvolnenies_30','information_of_uvolnenies_31','information_of_uvolnenies_32'
                    ,'information_of_uvolnenies_33','information_of_uvolnenies_34','information_of_uvolnenies_35','information_of_uvolnenies_36'
                    ,'information_of_uvolnenies_37','information_of_uvolnenies_38','information_of_uvolnenies_39','information_of_uvolnenies_40']
        labels = {'information_of_uvolnenies_1': '1','information_of_uvolnenies_2': '2','information_of_uvolnenies_3': '3','information_of_uvolnenies_4': '4'
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

class uvolneniesMestoModelForm(forms.ModelForm):
    class Meta:
        model = uvolnenies
        fields = ['info_of_uvolnenies_1_mesto','info_of_uvolnenies_2_mesto','info_of_uvolnenies_3_mesto','info_of_uvolnenies_4_mesto'
                    ,'info_of_uvolnenies_5_mesto','info_of_uvolnenies_6_mesto','info_of_uvolnenies_7_mesto','info_of_uvolnenies_8_mesto'
                    ,'info_of_uvolnenies_9_mesto','info_of_uvolnenies_10_mesto','info_of_uvolnenies_11_mesto','info_of_uvolnenies_12_mesto'
                    ,'info_of_uvolnenies_13_mesto','info_of_uvolnenies_14_mesto','info_of_uvolnenies_15_mesto','info_of_uvolnenies_16_mesto'
                    ,'info_of_uvolnenies_17_mesto','info_of_uvolnenies_18_mesto','info_of_uvolnenies_19_mesto','info_of_uvolnenies_20_mesto'
                    ,'info_of_uvolnenies_21_mesto','info_of_uvolnenies_22_mesto','info_of_uvolnenies_23_mesto','info_of_uvolnenies_24_mesto'
                    ,'info_of_uvolnenies_25_mesto','info_of_uvolnenies_26_mesto','info_of_uvolnenies_27_mesto','info_of_uvolnenies_28_mesto'
                    ,'info_of_uvolnenies_29_mesto','info_of_uvolnenies_30_mesto','info_of_uvolnenies_31_mesto','info_of_uvolnenies_32_mesto'
                    ,'info_of_uvolnenies_33_mesto','info_of_uvolnenies_34_mesto','info_of_uvolnenies_35_mesto','info_of_uvolnenies_36_mesto'
                    ,'info_of_uvolnenies_37_mesto','info_of_uvolnenies_38_mesto','info_of_uvolnenies_39_mesto','info_of_uvolnenies_40_mesto']
        labels = {'info_of_uvolnenies_1_mesto': '','info_of_uvolnenies_2_mesto': '','info_of_uvolnenies_3_mesto': '','info_of_uvolnenies_4_mesto': ''
                    ,'info_of_uvolnenies_5_mesto': '','info_of_uvolnenies_6_mesto': '','info_of_uvolnenies_7_mesto': '','info_of_uvolnenies_8_mesto': ''
                    ,'info_of_uvolnenies_9_mesto': '','info_of_uvolnenies_10_mesto': '','info_of_uvolnenies_11_mesto': '','info_of_uvolnenies_12_mesto': ''
                    ,'info_of_uvolnenies_13_mesto': '','info_of_uvolnenies_14_mesto': '','info_of_uvolnenies_15_mesto': '','info_of_uvolnenies_16_mesto': ''
                    ,'info_of_uvolnenies_17_mesto': '','info_of_uvolnenies_18_mesto': '','info_of_uvolnenies_19_mesto': '','info_of_uvolnenies_20_mesto': ''
                    ,'info_of_uvolnenies_21_mesto': '','info_of_uvolnenies_22_mesto': '','info_of_uvolnenies_23_mesto': '','info_of_uvolnenies_24_mesto': ''
                    ,'info_of_uvolnenies_25_mesto': '','info_of_uvolnenies_26_mesto': '','info_of_uvolnenies_27_mesto': '','info_of_uvolnenies_28_mesto': ''
                    ,'info_of_uvolnenies_29_mesto': '','info_of_uvolnenies_30_mesto': '','info_of_uvolnenies_31_mesto': '','info_of_uvolnenies_32_mesto': ''
                    ,'info_of_uvolnenies_33_mesto': '','info_of_uvolnenies_34_mesto': '','info_of_uvolnenies_35_mesto': '','info_of_uvolnenies_36_mesto': ''
                    ,'info_of_uvolnenies_37_mesto': '','info_of_uvolnenies_38_mesto': '','info_of_uvolnenies_39_mesto': '','info_of_uvolnenies_40_mesto': ''
        }

class uvolneniesVremyaModelForm(forms.ModelForm):
    class Meta:
        model = uvolnenies
        fields = ['info_of_uvolnenies_1_vremya','info_of_uvolnenies_2_vremya','info_of_uvolnenies_3_vremya','info_of_uvolnenies_4_vremya'
                    ,'info_of_uvolnenies_5_vremya','info_of_uvolnenies_6_vremya','info_of_uvolnenies_7_vremya','info_of_uvolnenies_8_vremya'
                    ,'info_of_uvolnenies_9_vremya','info_of_uvolnenies_10_vremya','info_of_uvolnenies_11_vremya','info_of_uvolnenies_12_vremya'
                    ,'info_of_uvolnenies_13_vremya','info_of_uvolnenies_14_vremya','info_of_uvolnenies_15_vremya','info_of_uvolnenies_16_vremya'
                    ,'info_of_uvolnenies_17_vremya','info_of_uvolnenies_18_vremya','info_of_uvolnenies_19_vremya','info_of_uvolnenies_20_vremya'
                    ,'info_of_uvolnenies_21_vremya','info_of_uvolnenies_22_vremya','info_of_uvolnenies_23_vremya','info_of_uvolnenies_24_vremya'
                    ,'info_of_uvolnenies_25_vremya','info_of_uvolnenies_26_vremya','info_of_uvolnenies_27_vremya','info_of_uvolnenies_28_vremya'
                    ,'info_of_uvolnenies_29_vremya','info_of_uvolnenies_30_vremya','info_of_uvolnenies_31_vremya','info_of_uvolnenies_32_vremya'
                    ,'info_of_uvolnenies_33_vremya','info_of_uvolnenies_34_vremya','info_of_uvolnenies_35_vremya','info_of_uvolnenies_36_vremya'
                    ,'info_of_uvolnenies_37_vremya','info_of_uvolnenies_38_vremya','info_of_uvolnenies_39_vremya','info_of_uvolnenies_40_vremya']
        labels = {'info_of_uvolnenies_1_vremya': '','info_of_uvolnenies_2_vremya': '','info_of_uvolnenies_3_vremya': '','info_of_uvolnenies_4_vremya': ''
                    ,'info_of_uvolnenies_5_vremya': '','info_of_uvolnenies_6_vremya': '','info_of_uvolnenies_7_vremya': '','info_of_uvolnenies_8_vremya': ''
                    ,'info_of_uvolnenies_9_vremya': '','info_of_uvolnenies_10_vremya': '','info_of_uvolnenies_11_vremya': '','info_of_uvolnenies_12_vremya': ''
                    ,'info_of_uvolnenies_13_vremya': '','info_of_uvolnenies_14_vremya': '','info_of_uvolnenies_15_vremya': '','info_of_uvolnenies_16_vremya': ''
                    ,'info_of_uvolnenies_17_vremya': '','info_of_uvolnenies_18_vremya': '','info_of_uvolnenies_19_vremya': '','info_of_uvolnenies_20_vremya': ''
                    ,'info_of_uvolnenies_21_vremya': '','info_of_uvolnenies_22_vremya': '','info_of_uvolnenies_23_vremya': '','info_of_uvolnenies_24_vremya': ''
                    ,'info_of_uvolnenies_25_vremya': '','info_of_uvolnenies_26_vremya': '','info_of_uvolnenies_27_vremya': '','info_of_uvolnenies_28_vremya': ''
                    ,'info_of_uvolnenies_29_vremya': '','info_of_uvolnenies_30_vremya': '','info_of_uvolnenies_31_vremya': '','info_of_uvolnenies_32_vremya': ''
                    ,'info_of_uvolnenies_33_vremya': '','info_of_uvolnenies_34_vremya': '','info_of_uvolnenies_35_vremya': '','info_of_uvolnenies_36_vremya': ''
                    ,'info_of_uvolnenies_37_vremya': '','info_of_uvolnenies_38_vremya': '','info_of_uvolnenies_39_vremya': '','info_of_uvolnenies_40_vremya': ''
        }








#Отпуск--
class otpusksModelForm(forms.ModelForm):
    class Meta:
        model = otpusks
        fields = ['information_of_otpusks_1','information_of_otpusks_2','information_of_otpusks_3','information_of_otpusks_4'
                    ,'information_of_otpusks_5','information_of_otpusks_6','information_of_otpusks_7','information_of_otpusks_8'
                    ,'information_of_otpusks_9','information_of_otpusks_10','information_of_otpusks_11','information_of_otpusks_12'
                    ,'information_of_otpusks_13','information_of_otpusks_14','information_of_otpusks_15','information_of_otpusks_16'
                    ,'information_of_otpusks_17','information_of_otpusks_18','information_of_otpusks_19','information_of_otpusks_20'
                    ,'information_of_otpusks_21','information_of_otpusks_22','information_of_otpusks_23','information_of_otpusks_24'
                    ,'information_of_otpusks_25','information_of_otpusks_26','information_of_otpusks_27','information_of_otpusks_28'
                    ,'information_of_otpusks_29','information_of_otpusks_30','information_of_otpusks_31','information_of_otpusks_32'
                    ,'information_of_otpusks_33','information_of_otpusks_34','information_of_otpusks_35','information_of_otpusks_36'
                    ,'information_of_otpusks_37','information_of_otpusks_38','information_of_otpusks_39','information_of_otpusks_40']
        labels = {'information_of_otpusks_1': '1','information_of_otpusks_2': '2','information_of_otpusks_3': '3','information_of_otpusks_4': '4'
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

class otpusksMestoModelForm(forms.ModelForm):
    class Meta:
        model = otpusks
        fields = ['info_of_otpusks_1_mesto','info_of_otpusks_2_mesto','info_of_otpusks_3_mesto','info_of_otpusks_4_mesto'
                    ,'info_of_otpusks_5_mesto','info_of_otpusks_6_mesto','info_of_otpusks_7_mesto','info_of_otpusks_8_mesto'
                    ,'info_of_otpusks_9_mesto','info_of_otpusks_10_mesto','info_of_otpusks_11_mesto','info_of_otpusks_12_mesto'
                    ,'info_of_otpusks_13_mesto','info_of_otpusks_14_mesto','info_of_otpusks_15_mesto','info_of_otpusks_16_mesto'
                    ,'info_of_otpusks_17_mesto','info_of_otpusks_18_mesto','info_of_otpusks_19_mesto','info_of_otpusks_20_mesto'
                    ,'info_of_otpusks_21_mesto','info_of_otpusks_22_mesto','info_of_otpusks_23_mesto','info_of_otpusks_24_mesto'
                    ,'info_of_otpusks_25_mesto','info_of_otpusks_26_mesto','info_of_otpusks_27_mesto','info_of_otpusks_28_mesto'
                    ,'info_of_otpusks_29_mesto','info_of_otpusks_30_mesto','info_of_otpusks_31_mesto','info_of_otpusks_32_mesto'
                    ,'info_of_otpusks_33_mesto','info_of_otpusks_34_mesto','info_of_otpusks_35_mesto','info_of_otpusks_36_mesto'
                    ,'info_of_otpusks_37_mesto','info_of_otpusks_38_mesto','info_of_otpusks_39_mesto','info_of_otpusks_40_mesto']
        labels = {'info_of_otpusks_1_mesto': '','info_of_otpusks_2_mesto': '','info_of_otpusks_3_mesto': '','info_of_otpusks_4_mesto': ''
                    ,'info_of_otpusks_5_mesto': '','info_of_otpusks_6_mesto': '','info_of_otpusks_7_mesto': '','info_of_otpusks_8_mesto': ''
                    ,'info_of_otpusks_9_mesto': '','info_of_otpusks_10_mesto': '','info_of_otpusks_11_mesto': '','info_of_otpusks_12_mesto': ''
                    ,'info_of_otpusks_13_mesto': '','info_of_otpusks_14_mesto': '','info_of_otpusks_15_mesto': '','info_of_otpusks_16_mesto': ''
                    ,'info_of_otpusks_17_mesto': '','info_of_otpusks_18_mesto': '','info_of_otpusks_19_mesto': '','info_of_otpusks_20_mesto': ''
                    ,'info_of_otpusks_21_mesto': '','info_of_otpusks_22_mesto': '','info_of_otpusks_23_mesto': '','info_of_otpusks_24_mesto': ''
                    ,'info_of_otpusks_25_mesto': '','info_of_otpusks_26_mesto': '','info_of_otpusks_27_mesto': '','info_of_otpusks_28_mesto': ''
                    ,'info_of_otpusks_29_mesto': '','info_of_otpusks_30_mesto': '','info_of_otpusks_31_mesto': '','info_of_otpusks_32_mesto': ''
                    ,'info_of_otpusks_33_mesto': '','info_of_otpusks_34_mesto': '','info_of_otpusks_35_mesto': '','info_of_otpusks_36_mesto': ''
                    ,'info_of_otpusks_37_mesto': '','info_of_otpusks_38_mesto': '','info_of_otpusks_39_mesto': '','info_of_otpusks_40_mesto': ''
        }

class otpusksVremyaModelForm(forms.ModelForm):
    class Meta:
        model = otpusks
        fields = ['info_of_otpusks_1_vremya','info_of_otpusks_2_vremya','info_of_otpusks_3_vremya','info_of_otpusks_4_vremya'
                    ,'info_of_otpusks_5_vremya','info_of_otpusks_6_vremya','info_of_otpusks_7_vremya','info_of_otpusks_8_vremya'
                    ,'info_of_otpusks_9_vremya','info_of_otpusks_10_vremya','info_of_otpusks_11_vremya','info_of_otpusks_12_vremya'
                    ,'info_of_otpusks_13_vremya','info_of_otpusks_14_vremya','info_of_otpusks_15_vremya','info_of_otpusks_16_vremya'
                    ,'info_of_otpusks_17_vremya','info_of_otpusks_18_vremya','info_of_otpusks_19_vremya','info_of_otpusks_20_vremya'
                    ,'info_of_otpusks_21_vremya','info_of_otpusks_22_vremya','info_of_otpusks_23_vremya','info_of_otpusks_24_vremya'
                    ,'info_of_otpusks_25_vremya','info_of_otpusks_26_vremya','info_of_otpusks_27_vremya','info_of_otpusks_28_vremya'
                    ,'info_of_otpusks_29_vremya','info_of_otpusks_30_vremya','info_of_otpusks_31_vremya','info_of_otpusks_32_vremya'
                    ,'info_of_otpusks_33_vremya','info_of_otpusks_34_vremya','info_of_otpusks_35_vremya','info_of_otpusks_36_vremya'
                    ,'info_of_otpusks_37_vremya','info_of_otpusks_38_vremya','info_of_otpusks_39_vremya','info_of_otpusks_40_vremya'
        ]
        labels = {'info_of_otpusks_1_vremya': '','info_of_otpusks_2_vremya': '','info_of_otpusks_3_vremya': '','info_of_otpusks_4_vremya': ''
                    ,'info_of_otpusks_5_vremya': '','info_of_otpusks_6_vremya': '','info_of_otpusks_7_vremya': '','info_of_otpusks_8_vremya': ''
                    ,'info_of_otpusks_9_vremya': '','info_of_otpusks_10_vremya': '','info_of_otpusks_11_vremya': '','info_of_otpusks_12_vremya': ''
                    ,'info_of_otpusks_13_vremya': '','info_of_otpusks_14_vremya': '','info_of_otpusks_15_vremya': '','info_of_otpusks_16_vremya': ''
                    ,'info_of_otpusks_17_vremya': '','info_of_otpusks_18_vremya': '','info_of_otpusks_19_vremya': '','info_of_otpusks_20_vremya': ''
                    ,'info_of_otpusks_21_vremya': '','info_of_otpusks_22_vremya': '','info_of_otpusks_23_vremya': '','info_of_otpusks_24_vremya': ''
                    ,'info_of_otpusks_25_vremya': '','info_of_otpusks_26_vremya': '','info_of_otpusks_27_vremya': '','info_of_otpusks_28_vremya': ''
                    ,'info_of_otpusks_29_vremya': '','info_of_otpusks_30_vremya': '','info_of_otpusks_31_vremya': '','info_of_otpusks_32_vremya': ''
                    ,'info_of_otpusks_33_vremya': '','info_of_otpusks_34_vremya': '','info_of_otpusks_35_vremya': '','info_of_otpusks_36_vremya': ''
                    ,'info_of_otpusks_37_vremya': '','info_of_otpusks_38_vremya': '','info_of_otpusks_39_vremya': '','info_of_otpusks_40_vremya': ''}