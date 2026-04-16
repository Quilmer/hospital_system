from database import get_connection


def add_patient(name, birth_date, phone):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO patients (name, birth_date, phone) VALUES (%s,%s,%s)"
    cursor.execute(query, (name, birth_date, phone))

    print("Paciente guardado na BD!") 

    cursor.close()
    conn.close()

def list_patients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def add_doctor(name, specialty):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO doctors (name, specialty) VALUES (%s,%s)"
    cursor.execute(query, (name, specialty))
    conn.commit()
    conn.close()

def list_doctors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def add_appointment(patient_id, doctor_id, date, reason):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO appointments (patient_id, doctor_id, appointment_date, reason)
        VALUES (%s,%s,%s,%s)
    """
    cursor.execute(query, (patient_id, doctor_id, date, reason))
    conn.commit()
    conn.close()

def test_insert():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO patients (name, birth_date, phone) VALUES ('TESTE', '2000-01-01', '000')")
    conn.commit()

    print("INSERT MANUAL FEITO")

    cursor.close()
    conn.close()

def medical_history(patient_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT a.id, d.name, a.appointment_date, a.reason, a.diagnosis, a.prescription
        FROM appointments a
        JOIN doctors d ON a.doctor_id = d.id
        WHERE patient_id = %s
        ORDER BY appointment_date DESC
    """
    cursor.execute(query, (patient_id,))
    for row in cursor.fetchall():
        print(row)
    conn.close()