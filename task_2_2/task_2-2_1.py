
course_name = "Informatics"    
current_stage = 2                
completed_tasks = 5              


print(f"Course: {course_name} | Stage: {current_stage} | Completed tasks: {completed_tasks}")
print()


text_with_space = "   Hola   "
print(f"Before: '{text_with_space}'")

text_without_space = text_with_space.strip()
print(f"After: '{text_without_space}'")
print()


text_small = "atgc"
print(f"Before: {text_small}")

text_big = text_small.upper()
print(f"After: {text_big}")
print()


datos_dirty = "   atgcatgc   "
print(f"Before: '{datos_dirty}'")

datos_cleans = datos_dirty.strip().upper()
print(f"After: {datos_cleans}")
print()


nombre = "Damaris"
edad = 22

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print()