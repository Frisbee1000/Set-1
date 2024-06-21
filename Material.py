def material_waste(total_material, material_units, num_jobs, job_consumption):
    Pass1 = int(num_jobs) * int(job_consumption)
    Pass2 = total_material - Pass1
    Final = str(Pass2)+(material_units)
    return(Final)

str(material_waste(100,"kg",5,2))