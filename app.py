from flask import Flask, render_template, flash, request, redirect, url_for
from CrawlerInterface import *
from DataExportInterface import *
from AttributeGenerator import *
from werkzeug.utils import secure_filename
import os
from config import *
from flask import abort,jsonify

app = Flask(__name__)
cc = CrawlerController()
db = InformationManager(config.local_db)

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'xls', 'xlsx', 'csv', 'psv']) # for att/doc list uploads
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/index')
def index():

    # At this point, we need to pull all of the ruleset names and psudo-keys
    rulesets = {1: {'name': 'Furniture'}, 2: {'name': 'Cars'}, 3: {'name': 'Phones'}, 4: {'name': 'Watches'}}

    return render_template('index2.html', rulesets=rulesets)

@app.route('/search')
def emptySearch():
    return abort(404)

@app.route('/search/<ruleset>')
def showSearch(ruleset=None):

    # At this point, we need to pull the data from the DB and build a data table from it using the ruleset selected

    header = ['Name', 'Position', 'Office', 'Age', 'Start date', 'Salary'] # example header

    data = {1: {'Name': 'Joshua Kirby', 'Position': 'BS SwE Student', 'Office': 'Fredericton', 'Age': '22?', 'Start date': '2019/01/26', "Salary": '$0'}} # example data

    return render_template("results2.html", header=header, data=data)

@app.route('/admin')
def admin():
    # There should be authentication here but it's not to make dev easier

    return render_template('admin2.html')

@app.route('/executor')
def executor():

    # There should be data built to show all the rule and url sets

    rulesets = {1: {'name': 'Furniture'}, 2: {'name': 'Cars'}, 3: {'name': 'Phones'}, 4: {'name': 'Watches'}}

    urlsets = {1: {'name': 'Wikipedia'}, 2: {'name': 'AutoTrader'}, 3: {'name': 'Phone Websites'}, 4: {'name': 'The Fifth Watches'}, 5: {'name': 'Government of Canada'}, 6: {'name': 'Fake Websites'}, 7: {'name': 'Line Filler'}, 8: {'name': 'Images of Cats'}}

    return render_template('executor2.html', rulesets=rulesets, urlsets=urlsets)

@app.route('/run')
def run():
    # TODO check that these are int parameters, else convert them to int
    ruleset = request.args.get('Ruleset')
    urlset = request.args.get('URLset')
    crawldata = runcrawl(ruleset, urlset)
    tablename = db.exportDataframeToDB(crawldata, docid=urlset, attid=ruleset) # TODO this is the name of the table containing this crawl data
    return executor()

@app.route('/upload')
def upload():
    return render_template('/upload2.html')

@app.route('/file', methods=['POST'])
def file():

    val = request
    if 'file' not in request.files:
        error = "Missing data source!"
        return jsonify({'error': error})

    file = request.files['file']

    file.save('/home/joshua/Desktop/ExampleUpload')

    f = open(file)

    return upload()



def runcrawl(attid, docid):
    doclist = db.getDocumentListById(docid)
    attlist = db.getAttributeListById(attid)
    crawldata = cc.crawlDocuments(doclist, attlist)
    return crawldata




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ API Methods Below Here ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# before using this, user will need to define the attributes and document set to use.
@app.route('/api/invokecrawlerpreset/', methods = ['POST'])
def invoke_crawler_preset(docid, attid):
    doc = db.getDocumentListById(docid)
    att = db.getDocumentListById(attid)
    crawldata = cc.crawlDocuments(doc, att)
    return crawldata

@app.route('/api/uploadattributes/', methods = ['POST'])
def upload_attributes_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            attparser = AttributeFileParser(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            attdata = attparser.read_all_attributes()
            attid = db.addAttributeData(attdata, "Attribute Set: "+filename, filename)
            return attid



@app.errorhandler(404)
def errors():
    return "Oops, this should be a page but isn't!"