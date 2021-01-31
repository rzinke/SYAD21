#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "MPZinke"

########################################################################################################################
#                                                                                                                      #
#   created by: MPZinke                                                                                                #
#   on ..                                                                                                              #
#                                                                                                                      #
#   DESCRIPTION:                                                                                                       #
#   BUGS:                                                                                                              #
#   FUTURE:                                                                                                            #
#                                                                                                                      #
########################################################################################################################


def __CLOSE__(cnx, cursor):
	cursor.close();
	cnx.close();


def __CONNECT__(user : str, password : str, db_name : str):
	import mysql.connector;
	cnx = mysql.connector.connect(user=user, password=password, host="localhost", port="3306",  database=db_name);
	return cnx, cnx.cursor(buffered=True);


def __UTILITY__associate_query(cursor):
	headers = [header[0] for header in cursor._description];
	return [{header : (row[x] if row[x] else None) for x, header in enumerate(headers)} for row in cursor._rows];


def __UTILITY__query(cursor : object, query : str, *params) -> list:
	if(len(params)): cursor.execute(query, params);
	else: cursor.execute(query);
	return __UTILITY__associate_query(cursor);




def main():
	cnx, cursor = __CONNECT__("root", "mysql", "SYAD");
	query = "SELECT * FROM `Restaurant`;";
	restaurants = __UTILITY__query(cursor, query);
	print(restaurants, end="\n\n\n");

	# get corners for restaurants
	query = "SELECT * FROM `RestaurantPoints` WHERE `Restaurant.id` = %s;";
	for restaurant in restaurants:
		points = __UTILITY__query(cursor, query, restaurant["id"]);
		print(type(points))
		print(points[0]);
		print(points);

	__CLOSE__(cnx, cursor);



if __name__ == "__main__":
	main()
