from flask import Flask, render_template
 
app = Flask(__name__)

@app.route('/')
def homepage():

    title = "Epic Tutorials"
    paragraph = ["wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!","wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!"]

    try:
        return render_template("index.html", title = title, paragraph=paragraph)
    except Exception, e:
        return str(e)

@app.route('/about')
def aboutpage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("index.html", title=title, paragraph=paragraph, pageType=pageType)


@app.route('/about/contact')
def contactPage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("index.html", title=title, paragraph=paragraph, pageType=pageType)



@app.route('/graph')
def graph(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
    import sqlite3

    conn = sqlite3.connect('test.db')
    
    #conn.
    print "Opened database successfully", conn.__str__();
    
    #===============================================================================
    # /*conn.execute('''CREATE TABLE COMPANY
    #        (ID INT PRIMARY KEY     NOT NULL,
    #        NAME           TEXT    NOT NULL,
    #        AGE            INT     NOT NULL,
    #        ADDRESS        CHAR(50),
    #        SALARY         REAL);''')*/
    #===============================================================================
    #print "Table created successfully";
    
    cursor = conn.execute("select distinct country, count from OlympicsMedalData where year = 2016 and indicator = \'Total\' and country <> \'World\' order by count desc limit 3");
    countries = []
    medals1 = []
    medals2 = []
    medals3 = []
    years = []
    for row in cursor:
       print "country = ", row[0]
       countries.append(row[0])
       print "count = ", row[1], "\n"
    
    cursor = conn.execute("select count from OlympicsMedalData where year <= 2016 and year > 2000 and indicator = \'Total\' and country = \'" + countries[0] + "\' order by year asc");
    for row in cursor:
       print "medals = ", row[0]
       medals1.append(row[0])
       
    
    cursor = conn.execute("select year, count from OlympicsMedalData where year <= 2016 and year > 2000 and indicator = \'Total\' and country = \'" + countries[1] + "\' order by year asc");
    for row in cursor:
       print "years = ", row[0]
       print "medals = ", row[1]
       years.append(row[0])
       medals2.append(row[1])
       
    cursor = conn.execute("select count from OlympicsMedalData where year <= 2016 and year > 2000 and indicator = \'Total\' and country = \'" + countries[2] + "\' order by year asc");
    for row in cursor:
       print "medals = ", row[0]
       medals3.append(row[0])
       
    conn.close()
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": countries[0].__str__(), "data": medals1}, {"name": countries[1].__str__(), "data": medals2}, {"name": countries[2].__str__(), "data": medals3}]
    title = {"text": 'Medals in last 4 olympics by top 3 countries'}
    xAxis = {"categories": years}
    yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
 
if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)