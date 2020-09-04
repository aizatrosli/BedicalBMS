


raw_a="""
select diagnosisdate, bedical_diagnosis.department,
  case when bedical_bedmanagement.diagnosisid is null then 'Outpatient' else 'Inpatient' end as patienttype
from bedical_diagnosis left join bedical_bedmanagement
on bedical_diagnosis.diagnosisid = bedical_bedmanagement.diagnosisid
"""
raw_b="""
select to_char(diagnosisdate::date,'YYYY-MM') as dmonth, bedical_diagnosis.department,
  case when bedical_bedmanagement.diagnosisid is null then 'Outpatient' else 'Inpatient' end as patienttype,
  count(bedical_diagnosis.patientid) as patientcount
from bedical_diagnosis left join bedical_bedmanagement
on bedical_diagnosis.diagnosisid = bedical_bedmanagement.diagnosisid
group by to_char(diagnosisdate::date,'YYYY-MM'), bedical_diagnosis.department,
  case when bedical_bedmanagement.diagnosisid is null then 'Outpatient' else 'Inpatient' end
"""

raw_c="""
select admissiondate, department, date_part('day',age(dischargedate, admissiondate))+1 as los
from bedical_bedmanagement
where dischargedate is not null;

select a.admissionmonth, department, avg(los) as avg_los
from (
select to_char(admissiondate::date,'YYYY-MM') as admissionmonth, department,
date_part('day',age(dischargedate, admissiondate))+1 as los
from bedical_bedmanagement
where dischargedate is not null) as a
group by a.admissionmonth, department
"""

raw_d="""
select a.department,
sum(case when b.bedid is null then 1 else 0 end) as vacant,
sum(case when b.bedid is null then 0 else 1 end) as occupied
from bedical_bed as a left join
(select bedid, bedstatus from bedical_bedmanagement where dischargedate is null) as b
on a.bedid = b.bedid
group by a.department
"""

raw_e="""
select count(*) as total_discharge
from bedical_bedmanagement
where dischargedate is not null
"""

raw_f="""
select count(*) as total_admitted
from bedical_bedmanagement
"""
raw_g="""
select count(*) as available_beds
from bedical_bed as a left join
(select bedid, bedstatus from bedical_bedmanagement where dischargedate is null) as b
on a.bedid = b.bedid
where b.bedid is null
"""

raw_h="""
select count(*) as patient_emergency
from bedical_bedmanagement
where dischargedate is null
and department = 'Emergency'
"""

raw_i="""
select to_char(diagnosisdate::date,'YYYY-MM') as dmonth,
b.doctorfirstname||' '||b.doctorlastname as doctor,
count(patientid) admissioncount
from bedical_diagnosis a inner join bedical_doctor b
on a.doctorid = b.doctorid
group by to_char(diagnosisdate::date,'YYYY-MM'),
b.doctorfirstname||' '||b.doctorlastname
order by count(patientid) desc
"""

raw_j="""
select to_char(diagnosisdate::date,'YYYY-MM') as dmonth,
b.doctorfirstname||' '||b.doctorlastname as doctor,
count(patientid) admissioncount
from bedical_diagnosis a inner join bedical_doctor b
on a.doctorid = b.doctorid
where a.diagnosisid in (select diagnosisid from bedical_bedmanagement)
group by to_char(diagnosisdate::date,'YYYY-MM'),
b.doctorfirstname||' '||b.doctorlastname
order by count(patientid) desc
"""

raw_k="""
select count(*) as staffs from bedical_nurse
"""

raw_l="""
select sum(paymentamount) as cost from bedical_payment
"""