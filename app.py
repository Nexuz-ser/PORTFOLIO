from flask import Flask, render_template, request
import link_list
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template('works.html')

@app.route('/works/ToUpperCase', methods=['GET', 'POST'])
def upperCase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/works/area/circle', methods=['GET', 'POST'])
def acircle():
    result = None
    if request.method == 'POST':
        radius = request.form.get('radius', '')
        result = int(radius)*3.14*int(radius)
    return render_template('circle.html', result=result)

# @app.route('/areaOfcirle', methods=['GET', 'POST'])
# def areaOfcirle():
#     result = None
#     name=request.get('name','')
#     print(name)
#     if request.method == 'POST':
#         input_string = request.form.get('inputradius', '')
#         result = int(input_string) * int(input_string) * 3.14
#     return render_template('areaCircle.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/works/area/triangle', methods=['GET', 'POST'])
def atriangle():
    result = None
    if request.method == 'POST':
        base = request.form.get('base', '')
        height = request.form.get('height', '')
        result = (int(base)*int(height))/2
    return render_template('triangle.html', result=result)

Link_list = link_list.LinkedList()

@app.route('/works/Link-List', methods = ['GET', 'POST'])
def linkList():
    result = None
    status = None
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'Add':
            data = request.form.get('add_value', '')
            Link_list.insert_at_beginning(data)

        if action == 'Add_end':
            data = request.form.get('add_value', '')
            Link_list.insert_at_end(data)

        if action == 'search':
            data = request.form.get('search_node', '')
            if Link_list.search(data):
                status = 'True'
            else:
                status = 'False'

        if action == 'remove_at':
            data = request.form.get('remove_node', '')
            Link_list.remove_at(data)

        if action == 'remove_at_end':
            Link_list.remove_at_end()

        if action == 'remove_at_beginning':
            Link_list.remove_beginning()

        if action == "clear":
            Link_list.clear_all()
    
    return render_template('link_list.html',node = Link_list.printLinkedList(), result=result, status=status)


if __name__ == "__main__":
    app.run(debug=True)
