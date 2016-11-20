#!/usr/bin/python
 # -*- coding: utf-8 -*-
import codecs
import sqlite3 
conn = sqlite3.connect('datos_empleados.db') 
print "Base de datos conectada con exito"; 
sql1='''
SELECT nombre,salario,id FROM empleado;
'''
cursor1 = conn.execute(sql1)
sql2='''
SELECT descripcion,desde,hasta,porcentaje_aplica,exceso,cuota_fija FROM tramo
'''
cursor2 = conn.execute(sql2)
tramo1=0
tramo2=0
tramo3=0
tramo4=0
descTram2=[]
x=0
for rowempleado in cursor1:
	x+=1
	if rowempleado[1]>0.01 and rowempleado[1]<= 472.00:
		tramo1+=1
		print "Categoria: TRAMO 1"
		print 'nombre: ', rowempleado[0]
		print 'salario: ', rowempleado[1]
		afp=rowempleado[1]*0.0625
		isss=rowempleado[1]*0.03
		salario_neto=rowempleado[1]-isss-afp
		id_empleado=rowempleado[2]
		nombre_empleado=rowempleado[0]
		conn.execute("INSERT INTO pago_empleado(id_empleado,descuento_afp,descuento_isss,renta,salario_neto) VALUES (?,?,?,?,?)",  (id_empleado,round(afp,2),round(isss,2),0,round(salario_neto,2)))
		print '-------------------------------------------------'
	if rowempleado[1]>472.00 and rowempleado[1]< 895.24:
		tramo2+=1
		print "Categoria: TRAMO 2"
		print 'nombre: ', rowempleado[0]
		print 'salario: ', rowempleado[1]
		afp=rowempleado[1]*0.0625
		isss=rowempleado[1]*0.03
		
		id_empleado=rowempleado[2]
		nombre_empleado=rowempleado[0]
		exceso=rowempleado[1]-472.00
		total_tramo=exceso*0.10
		total_exceso=total_tramo+17.67
		salario_neto=rowempleado[1]-isss-afp-total_exceso
		print 'exceso: ',exceso,'total tramo: ',total_tramo,'total exceso: ',total_exceso
		
		conn.execute("INSERT INTO pago_empleado(id_empleado,descuento_afp,descuento_isss,renta,salario_neto) VALUES (?,?,?,?,?)",  (id_empleado,round(afp,2),round(isss,2),round(total_exceso,2),round(salario_neto,2)))
		print '-------------------------------------------------'
	if rowempleado[1]>895.24 and rowempleado[1]< 2038.10:
		tramo3+=1
		print "Categoria: TRAMO 3"
		print 'nombre: ', rowempleado[0]
		print 'salario: ', rowempleado[1]
		afp=rowempleado[1]*0.0625
		isss=rowempleado[1]*0.03
		
		id_empleado=rowempleado[2]
		nombre_empleado=rowempleado[0]
		exceso=rowempleado[1]-895.24
		total_tramo=exceso*0.20
		total_exceso=total_tramo+60.00
		salario_neto=rowempleado[1]-isss-afp-total_exceso
		print 'exceso: ',exceso,'total tramo: ',total_tramo,'total exceso: ',total_exceso
		conn.execute("INSERT INTO pago_empleado(id_empleado,descuento_afp,descuento_isss,renta,salario_neto) VALUES (?,?,?,?,?)",  (id_empleado,round(afp,2),round(isss,2),round(total_exceso,2),round(salario_neto,2)))
		print '--------------------------------------------------'	
	if rowempleado[1]>2038.11:
		tramo4+=1
		print "Categoria: TRAMO 4"
		print 'nombre: ', rowempleado[0]
		print 'salario: ', rowempleado[1]
		afp=rowempleado[1]*0.0625
		isss=rowempleado[1]*0.03
		
		id_empleado=rowempleado[2]
		nombre_empleado=rowempleado[0]
		exceso=rowempleado[1]-2038.10
		total_tramo=exceso*0.30
		total_exceso=total_tramo+288.57
		salario_neto=rowempleado[1]-isss-afp-total_exceso
		print 'exceso: ',exceso,'total tramo: ',total_tramo,'total exceso: ',total_exceso
		conn.execute("INSERT INTO pago_empleado(id_empleado,descuento_afp,descuento_isss,renta,salario_neto) VALUES (?,?,?,?,?)",  (id_empleado,round(afp,2),round(isss,2),round(total_exceso,2),round(salario_neto,2)))	
		print '---------------------------------------------------'
		
print 'empleados en tramo 1: ',tramo1
print 'empleados en tramo 2: ',tramo2
print 'empleados en tramo 3: ',tramo3
print 'empleados en tramo 4: ',tramo4



conn.commit()  			  
conn.close()

