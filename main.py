import services
import models

def menu():
    while True:
        print("\n=== SISTEMA HOSPITAL ===")
        print("1 - Registar Paciente")
        print("2 - Listar Pacientes")
        print("3 - Registar Médico")
        print("4 - Listar Médicos")
        print("5 - Marcar Consulta")
        print("6 - Histórico Médico")
        #print("7 - TESTE INSERT")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            services.register_patient()
        elif op == "2":
            models.list_patients()
        elif op == "3":
            services.register_doctor()
        elif op == "4":
            models.list_doctors()
        elif op == "5":
            services.schedule_appointment()
        elif op == "6":
            services.show_history()
        elif op == "7":
            models.test_insert()
        elif op == "0":
            break

menu()