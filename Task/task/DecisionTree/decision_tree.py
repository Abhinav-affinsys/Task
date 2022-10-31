import yaml
import os 
loc = '/home/abhinav-dev/task-django/Task/task/DecisionTree'
class DecisionTree:

    def __init__(self, filename):

        filename = filename
        with open(filename, 'r') as stream:
            try:
                decisions = yaml.load(stream, Loader=yaml.FullLoader)
            except yaml.YAMLError as exc:
                print(exc)

        self.decisions = decisions

    def get_decisions(self):
        return self.decisions

    def _validator(self, user_data, product_data, validation):
        is_cat = 0  # Numeric
        if validation['attribute_of'] == 'user':
            try:
                # print(validation['attribute'])
                value = float(user_data[validation['attribute']])
                # print(validation['attribute'])
            except:
                value = user_data[validation['attribute']].split(',')
                is_cat = 1
                # print(value, type(value))

        else:
            value = product_data[validation['attribute']].split(',')

        # print(validation,type(validation['allowed_values']))
        if 'allowed_values' in validation:
            for criteria in validation['allowed_values']:
                # print(criteria)

                if validation['allowed_values'][criteria] == False:
                    # print(criteria)
                    continue

                elif criteria == 'min' and value < validation['allowed_values'][criteria] and not is_cat:
                    # print('Min')
                    return False

                elif criteria == 'max' and value > validation['allowed_values'][criteria] and not is_cat:
                    # print('Max')
                    return False

                elif criteria == 'list':# and value not in validation['allowed_values'][criteria]:
                    allowed_value_list = validation['allowed_values'][criteria].split(',')
                    # print(allowed_value_list,value)
                    if set(value).intersection(set(allowed_value_list)) == set():
                        return False

        if 'excluded_values' in validation:
            for criteria in validation['excluded_values']:

                if validation['excluded_values'][criteria] == False:
                    continue

                if criteria == 'min' and value > validation['excluded_values'][criteria] and not is_cat:
                    return False

                if criteria == 'max' and value < validation['excluded_values'][criteria] and not is_cat:
                    return False

                if criteria == 'list' and value in validation['excluded_values'][criteria]:
                   return False
        return True

    def read_yaml_restrictions(self, filename):

        with open(loc+'/persona/'+filename, 'r') as stream:
            try:
                decisions = yaml.load(stream, Loader=yaml.FullLoader)

            except yaml.YAMLError as exc:
                print(exc)
                return None

        return decisions['restrictions']

    def validate_user_for_product(self, user_data, product_data, decisions, category, product):

        for i in range(len(decisions['products'])):
            if category != decisions['products'][i]['category']:
                continue

            for prod in decisions['products'][i]['product']:
                # print(product)
                # print(prod['id'],product)
                # if prod['id'] == product:
                    restrictions = self.read_yaml_restrictions(prod['restrictions'])
                    ret_val = True
                    for restriction in restrictions:
                        # print(prod['value'])
                        if self._validator(user_data, product_data, restriction) == False:
                            ret_val = False
                    return ret_val
        return True

    def validate_persona_for_user(self, persona_data, user_data, decisions, category, persona):

        for i in range(len(decisions['users'])):
            if category != decisions['users'][i]['category']:
                continue

            for per in decisions['users'][i]['persona']:
                # if per['id'] == persona:
                    restrictions = self.read_yaml_restrictions(per['restrictions'])
                    for restriction in restrictions:
                        # print(restriction)
                        if self._validator(user_data, persona_data, restriction) == False:
                            return False
        return True