# Import the driver.
import psycopg2

def create_table(database_, user_, host_, port_):
	# Connect to the "bank" database.
	conn = psycopg2.connect(database= database_, user= user_, host= host_, port= port_)

	# Make each statement commit immediately.
	conn.set_session(autocommit=True)

	# Open a cursor to perform database operations.
	cur = conn.cursor()
	# Create the "accounts" table.
	cur.execute("CREATE TABLE IF NOT EXISTS doppelganger.images (url STRING, hash BYTES PRIMARY KEY, img BLOB)")
	# Close the database connection.
	cur.close()
	conn.close()


def add_to_db(database_, user_, host_, port_, url_, hash_):
	# Connect to the "bank" database.
	conn = psycopg2.connect(database=database_, user=user_, host=host_, port=port_)

	# Make each statement commit immediately.
	conn.set_session(autocommit=True)

	# Open a cursor to perform database operations.
	cur = conn.cursor()
	# Insert two rows into the "accounts" table.
	cur.execute("INSERT INTO images (url, hash) VALUES('random', %s)" %hash_)

	# Close the database connection.
	cur.close()
	conn.close()

def find_match_from_db():
	return True

if __name__ == "__main__":
	create_table('doppelganger', 'test', 'localhost', 26257)

	add_to_db('doppelganger', 'test', 'localhost', 26257, "random", b'\\x02\\x00\\x00 \\x11\\x06l?\\xdb\\xff\\xff\\x1f8\\x8d\\xbc?g\\xff\\xff\\xdf\\xfe\\x8e\\xc1?\\x1d\\x00\\x00@\\x86\\x8d\\xb6\\xbf\\x15\\x00\\x00\\xc0\\x0f}\\xa9\\xbf\\x13\\x00\\x00\\x00\\\'?\\xa3\\xbf\\x13\\x00\\x00`\\xfe\\x02\\xb2\\xbf\\xfe\\xff\\xff\\xff\\x94\\x99\\xb8\\xbf\\x9e\\xff\\xff\\x7f\\x7f+\\xc0\\xbf\\xe3\\xff\\xff_\\x8e\\x8d\\xb0?\\x95\\x00\\x00 \\x17m\\xc0?\\xd1\\xff\\xff\\x1f\\x1e\\x00~\\xbf\\x06\\x00\\x00\\xc0\\x8d>\\xa7?\\x08\\x00\\x00 \\x9fx\\xb4?\\x16\\x00\\x00\\xc0\\xa2\\xad\\xb2?!\\x00\\x00 C\\xb6\\xb0?C\\x00\\x00 \\t\\xdb\\xa4\\xbf\\xf8\\xff\\xff\\xbf\\xda\\xd7\\xa9?5\\x00\\x00\\xa0ZI\\x97?\\xf7\\xff\\xff\\x7f\\\'\\xc9\\xb2\\xbf\\xfe\\xff\\xff_\\x13\\xb3\\xaf?\\xb5\\xff\\xff\\xff2\\xf3\\xcc?\\xe4\\xff\\xff_\\xab\\x98\\xa0?0\\x00\\x00\\x00\\x17_\\x7f\\xbf\\xa4\\xff\\xff\\xbfj\\xe3\\x9e?\\x96\\x00\\x00 \\xbe\\x8a\\xc2?\\xec\\xff\\xff\\x9f\\xb3C\\xc2?\\xec\\xff\\xff?\\xdcA\\xb0?a\\xff\\xff\\xdf\\xc6\\xf1\\xc2?$\\x00\\x00`\\xa6d\\xc0?\\x02\\x00\\x00\\xe0=\\xb1\\xb8\\xbf \\x00\\x00\\x80s\\xe2\\xb4\\xbf3\\x00\\x00\\x00)w\\xa8?\\xe6\\xff\\xff\\xbf\\xc8!|\\xbf\\x13\\x00\\x00@\\xeeL\\xa8?\\x1c\\x00\\x00\\x80\\xce\\x19\\xb6\\xbf\\x17\\x00\\x00@by\\x8d\\xbf\\x87\\xff\\xff\\x1f\\x97\\xe4\\xbc?\\x9f\\x00\\x00@\\x04\\xb5\\xc7?\\xe5\\xff\\xff\\x7fb\\xce\\xc4?C\\x00\\x00\\xc0b\\x9d\\xc1\\xbf\\xf1\\xff\\xff\\xbfT\\x8b\\x9c?\\xdc\\xff\\xff\\x1f\\x86\\x98\\x8e\\xbf\\x1d\\x00\\x00\\xa0\\xa2.\\xb3?B\\x00\\x00\\xc0E\\xc8\\xaf\\xbff\\xff\\xff?\\xa5b\\x89\\xbfG\\x00\\x00\\x00\\xf7\\xc3\\xa1?\\x01\\x00\\x00\\xc0\\xcbF\\xb3\\xbf\\xb6\\xff\\xff_l\\xc3\\x9a\\xbf\\x1d\\x00\\x00\\xc0\\xb20\\xae\\xbf\\xc6\\xff\\xff\\xbfD\\xa5\\xc9?\\xd7\\xff\\xff\\xbf\\xecJ\\xc6?\\x84\\x00\\x00@:d\\xbb\\xbf\\r\\x00\\x00 \\x894\\xb3?\\x11\\x00\\x00`\\xf5\\x84\\xae\\xbfM\\xff\\xff\\xbfA%\\x88\\xbfM\\x01\\x00 Z\\xae\\xbd?\\x03\\x00\\x00\\xe0ZL\\xa3?\\xfe\\xff\\xff\\x1f\\xc2b\\xa9\\xbfG\\x00\\x00\\x80@\\xfa\\xa2?)\\x00\\x00 H\\xd6\\x9e\\xbf\\xf3\\xff\\xff_\\xa3\\xec\\xc8\\xbf\\xf0\\xff\\xff\\xbf\\xad%\\xab?,\\x00\\x00 =\\x83\\xc2?\\x19\\x00\\x00\\xc0&2x\\xbf\\xca\\x00\\x00@\\xcf\\xa3\\xb9\\xbf\\xb4\\x00\\x00`Ub^?\\xe0\\xff\\xff\\x1fpZ\\x9c?\\x8e\\xff\\xff\\xdf\\xfc,\\x9f?\\x04\\x00\\x00\\xc0"\\xc2\\xb3?)\\x00\\x00`h\\x9e\\xa9?\\x1b\\x00\\x00\\x00P\\xe0w\\xbf\\x0e\\x00\\x00\\xa0\\x85iq?\\xac\\xff\\xff?k\\x9a\\x9c\\xbf\\xea\\xff\\xff\\xff\\x0b$\\xb0?\\xdf\\xff\\xff\\x1f"\\x07\\xb3\\xbf\\xba\\xfe\\xff?\\x8d\\x14\\xbd\\xbf>\\x00\\x00`?Q\\xa7\\xbf\\x95\\xff\\xff?\\x9f\\xa2\\x91\\xbf\\x10\\x00\\x00 \\xcc$\\xc0?C\\x00\\x00@6D\\xc3?\\xca\\xff\\xff\\xbf\\xb0?c\\xbfz\\xff\\xff\\xbfw(\\xc4?\\r\\x00\\x00\\xa0\\xe6\\xfd\\xb4?\\x8c\\x00\\x00\\x00[C\\x8c\\xbf\\xb0\\x00\\x00\\x80B\\x16\\xc1\\xbf\\x01\\x00\\x00\\x00\\xd8\\xf9\\xa9?\\xce\\xff\\xff\\x7fQ?\\xac\\xbf\\\'\\\x00\\x00`_P\\x9a\\xbf\\x0c\\x00\\x00\\xc0x\\xf8u?\\xb3\\xff\\xff\\x1f\\xb0\\x16\\xc0\\xbfG\\x00\\x00\\xc0\\x1b\\xf1\\xa1\\xbf,\\x00\\x00\\xc0\\x96\\x0b\\xa1\\xbfv\\x00\\x00\\x80\\xc4\\x10\\xbf?\\xea\\xff\\xff\\xff\\xda\\x93\\xb4\\xbf4\\x00\\x00\\xc0\\xaf\\x1c\\xc1\\xbf\\xb9\\xff\\xff\\xff\\x92&\\xae\\xbf\\xe2\\xff\\xff_\\x85\\xe7\\xb5?\\xfc\\xff\\xff\\xbf\\xc4\\x93\\xb3?\\\'\\x00\\x00`.\\x90\\xa6\\xbf\\xc0\\xff\\xff\\xdf\\xa6\\xc4\\xa1\\xbf\\xb4\\xff\\xff\\xff\\x8b\\x05\\xc4?/\\x00\\x00 O\\xef\\x9a?e\\xff\\xff_\\xdd\\xda\\xbf?\\xbd\\xff\\xff\\x1f\\\\j\\xaa?\\x01\\x00\\x00\\xc0A^\\xb1\\xbf\\xed\\xff\\xff\\xbf\\xe0N\\xa2?(\\x00\\x00@\\x94\\x1b\\xa3?\\x8e\\x00\\x00\\xa0d\\xdb\\xc8?G\\x00\\x00\\x00\\xe3F\\xc3\\xbf7\\x00\\x00\\x80\\x84u\\xa3?\\xff\\xff\\xff\\xbf\\x0b\\x8fx?V\\x01\\x00`kY\\xbd\\xbf\\xbb\\xff\\xff\\xdfFs\\xc3?Y\\x00\\x00\\x80\\x11pj\\xbf.\\x00\\x00\\xe0V-\\xae?\\xee\\xff\\xff_OL~\\xbf\\xe6\\xfe\\xff\\xdf\\xe2\\xbd\\x8d?\\xe2\\xff\\xff\\x1fy\\x94\\xb6\\xbf\\xdf\\xff\\xff\\x7fox\\x85\\xbf:\\x00\\x00@E\\xa9\\xab?\\xf6\\xff\\xff?\\xfe(\\xa1\\xbf\\xd9\\xff\\xff\\x7f\\xc1\\x89\\xac\\xbf\\x01\\x00\\x00\\xc0\\x10P\\xba\\xbfD\\x00\\x00@S?\\xab?\\x16\\x00\\x00\\xc0,d\\xa6?\\x96\\x00\\x00\\xe0\\\'s\\xba?\\x9d\\x00\\x00\\x00y\\x00\\xbc?')