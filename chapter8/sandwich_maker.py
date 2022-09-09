import pyinputplus as pyip

prices_dict = {
    'wheat': 2,
    'white': 1,
    'sourdough': 3,
    'chicken': 2,
    'turkey': 3,
    'ham': 1,
    'tofu': 1,
    'cheddar': 1,
    'Swiss': 2,
    'mozzarella': 2,
    'mayo': 1,
    'mustard': 1,
    'lettuce': 1,
    'tomato': 1,
}
sandwich_price = 0

def prompt_single_item(item):
    global sandwich_price
    if  pyip.inputYesNo('Do you want ' + item + '?') == 'yes':
        sandwich_price += prices_dict[item]

bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough'], 'Please choose a bread type:\n')
sandwich_price += prices_dict[bread_type]

protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], 'Please choose a protein type:\n')
sandwich_price += prices_dict[protein_type]

if pyip.inputYesNo('Do you want cheese?') == 'yes':
    cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], 'Please choose a cheese type:\n')
    sandwich_price += prices_dict[cheese_type]

prompt_single_item('mayo')
prompt_single_item('mustard')
prompt_single_item('lettuce')
prompt_single_item('tomato')

sandwich_count = pyip.inputInt("How many sandwiches do you want?", min=1)
print('The price will be ' + str(sandwich_price * sandwich_count))