import models

def register_patient():
    name = input("Nome: ")
    birth = input("Data nascimento (YYYY-MM-DD): ")
    phone = input("Telefone: ")
    models.add_patient(name, birth, phone)
    print("Paciente registado!")

def register_doctor():
    name = input("Nome médico: ")
    specialty = input("Especialidade: ")
    models.add_doctor(name, specialty)
    print("Médico registado!")

def schedule_appointment():
    patient_id = input("ID Paciente: ")
    doctor_id = input("ID Médico: ")
    date = input("Data consulta (YYYY-MM-DD HH:MM): ")
    reason = input("Motivo: ")
    models.add_appointment(patient_id, doctor_id, date, reason)
    print("Consulta marcada!")

def show_history():
    patient_id = input("ID Paciente: ")
    models.medical_history(patient_id)