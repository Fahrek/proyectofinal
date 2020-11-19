from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
import pymysql


# Create your views here.
def vista_principal(request):
    params = {'nota': 'funciona'}
    return render(request, 'bienvenida.html', params)


def about(request):
    return render(request, 'about.html')


def insert_psycopg(request):
    conn = psycopg2.connect(dbname="tecnojob",
                            user="andres",
                            password="1234")
    cursor = conn.cursor()
    sql = "insert into offer (title, company, salary, salary_min, salary_max, fecha, descript, url, remote) values (" \
          "'sql', 'binladen', 20000, 25000, 30000, '2020/02/08', 'adsfadsfadsf', 'https://buscajob.org', " \
          "false ); "
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

    with open("debug.log", "a+") as debug_file:
        print("RIC: Registro Insertado Correctamente", file=debug_file)
    return HttpResponse('Registro Insertado')


def insert_pymysql(request):
    conn = pymysql.connect('localhost', 'andres', '47601469', 'searchjob')

    cursor = conn.cursor()
    sql = "insert into offer (title, company, salary, salary_min, salary_max, fecha, descript, url, remote) values (" \
          "'sql', 'trustme', 30000, 35000, 36000, '2020/07/12', 'ghgfdjhhgdjhgf', 'https://buscajob.org', true ); "
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

    with open("debug.log", "a+") as debug_file:
        print("RIC: Registro Insertado Correctamente", file=debug_file)
    return HttpResponse('Registro Insertado')


def select_psycopg(request):
    conn = psycopg2.connect(dbname="tecnojob",
                            user="andres",
                            password="1234")
    cursor = conn.cursor()
    sql = "select * from offer"
    cursor.execute(sql)
    result = cursor.fetchone()

    # html = '<html>'
    # columns = [col[0] for col in cursor.description]
    # for column in columns:
    #     html += str(column) + '|'
    # html += '<br>'
    # for empleado in cursor.fetchall():
    #     for columna in empleado:
    #         html += str(columna) + '|'
    #     html += '<br>'
    # html += '</html>'

    cursor.close()
    conn.close()
    return HttpResponse(html)


def select_pymysql(request):
    conn = pymysql.connect('localhost', 'andres', '47601469', 'searchjob')
    cursor = conn.cursor()
    sql = "select * from offer"
    cursor.execute(sql)
    html = '<html>'
    columns = [col[0] for col in cursor.description]
    for column in columns:
        html += str(column) + '|'
    html += '<br>'
    for empleado in cursor.fetchall():
        for columna in empleado:
            html += str(columna) + '|'
        html += '<br>'
    html += '</html>'
    cursor.close()
    conn.close()
    return HttpResponse(html)


def delete_psycopg(request, offer_id):
    conn = psycopg2.connect(dbname="tecnojob",
                            user="andres",
                            password="1234")
    cursor = conn.cursor()
    sql = f"delete * from offer where offer_id = {offer_id}"
    cursor.execute(sql)


def delete_pymysql(request, offer_id):
    conn = pymysql.connect('localhost', 'andres', '47601469', 'searchjob')
    cursor = conn.cursor()
    sql = f"delete * from offer where offer_id = {offer_id}"
    cursor.execute(sql)


def vista_anadir(request):
    #prioridad = request.POST['name_prioridad']
    #titulo = request.POST['nombre_titulo']
    #nota = request.POST['name_nota']
    return redirect('home')

    #return HttpResponse(f'Insertado <br> prioridad: {prioridad} <br> titulo: {titulo} <br> nota: {nota}')

