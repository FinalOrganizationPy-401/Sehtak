# Sehtak

### Summary

It’s a platform for health history of the patients including the records of the deseases and hospitals, labs, x-rays centers and pharmacies.
The users in the medical centers can modify the patient data on their profile based on the permission level.

### PM

[Trello](https://trello.com/invite/b/QOAR26fX/d99bb528715f21ea6db061d759b5adf9/sehtak-health-platform)

### [Team-Agreement](mdFiles/Team_Agreement.md)

### [Software Requirements](mdFiles/requirements.md)

### [User Stories](mdFiles/userstories.md)

### [Domain Modeling](https://miro.com/app/board/uXjVPZAEcic=/?share_link_id=629488780212)

### [Database Schema Diagram](https://drawsql.app/teams/mohammad-azim/diagrams/sehtake)

### Members

 [Mohammad Azim](https://github.com/Mohammad99Azim)

 [Muhammad Qasem Tarboush](https://github.com/muhammadqasemtarboush1)

 [Lama Radwan](https://github.com/lamaradwan)

## API End points

---

### Patient

 Login: `/login`

Register: `/register`

Patient profile : `/profile/user ID/`

---

### Doctor

All Doctors : `/doctors/`

Doctor profile : `/doctors/profile/doctor ID/`

Edit Doctor profile : `/doctors/profile/edit/doctor ID/`

---

### Pharmacists

All Pharmacists : `/pharmacists/`

Pharmacist profile : `/pharmacist/profile/pharmacist ID/`

Edit Pharmacist profile : `/Pharmacists/profile/edit/Pharmacist ID/`

---

### labs

All labs : `/labs/`

lab profile : `/labs/profile/lab ID/`

Edit lab profile : `/labs/profile/edit/lab ID/`

---

### X_Ray labs

All X_Ray labs : `/x_rays/`

X_Ray lab profile : `/x_rays/profile/x_ray ID/`

Edit X_Ray lab profile : `/x_rays/profile/edit/x_ray lab ID/`

---

### Medicine

All Medicine : `/api/v1/medicine/`

Medicine details : `/api/v1/medicine/`

---

### Test

All Tests : `/api/v1/test/`

Test details : `/api/v1/test/ID/`

---

### X_Ray

All X_Ray : `/api/v1/x_ray/`

X_Ray details : `/api/v1/x_ray/ID/`

---

### Visits

View Patient visits: `api/v1/visits/`

Create New Visit: `api/v1/visits/create`

View visit details: `api/v1/visits/ visit id`
