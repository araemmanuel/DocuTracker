'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import axios from 'axios'

export default function BeneficiaryForm() {
  const router = useRouter()
  const [last_name, setLastName] = useState('')
  const [first_name, setFirstName] = useState('')
  const [middle_name, setMidName] = useState('')
  const [extension_name, setExtenName] = useState('')
  const [date_of_birth, setBirthday] = useState('')
  const [age, setAge] = useState('')
  const [gender, setGender] = useState('')
  const [contact_number, setContactNumber] = useState('')
  const [educational_attainment, setEducationalAttainment] = useState('')
  const [civil_status, setCivilStatus] = useState('')
  const [address, setAddress] = useState('')
  const API_URL = process.env.NEXT_PUBLIC_API_URL;

  const handleBeneficiary = async (e) => {
    console.log(`${API_URL}`);
    e.preventDefault()
    await axios.post(`${API_URL}/api/applic/create/`, {
      last_name,
      first_name,
      middle_name,
      extension_name,
      date_of_birth,
      age,
      gender,
      contact_number,
      educational_attainment,
      civil_status,
      address
    })
    router.push('/beneficiary')
  }

  return (
    <div className="max-w-xl mx-auto bg-white p-8 shadow rounded-lg">
      <h2 className="text-2xl font-bold mb-6 text-green-900">Beneficiary Form</h2>
      <form className="space-y-4" onSubmit={handleBeneficiary}>
        <div>
          <label>Full Name</label>
          <input type="text" placeholder="First Name" onChange={e => setFirstName(e.target.value)} />
          <input type="text" placeholder="Last Name" onChange={e => setLastName(e.target.value)} />
          <input type="text" placeholder="Middle Name" onChange={e => setMidName(e.target.value)} />
          <input type="text" placeholder="Extension Name" onChange={e => setExtenName(e.target.value)} />
        </div>
        <div>
          <label>Birthday</label>
          <input type="text" placeholder="Birthday" onChange={e => setBirthday(e.target.value)} />
        </div>
        <div>
          <label>Age</label>
          <input type="text" placeholder="Age" onChange={e => setAge(e.target.value)} />
        </div>
        <div>
          <label>Contact Number</label>
          <input type="text" placeholder="Contact Number"onChange={e => setContactNumber(e.target.value)} />
        </div>
        <div>
          <label>Gender</label>
          <input type="text" placeholder="Gender"onChange={e => setGender(e.target.value)} />
        </div>
        <div>
          <label>Educational Attainment</label>
          <input type="text" placeholder="Educational Attainment"onChange={e => setEducationalAttainment(e.target.value)} />
        </div>
        <div>
          <label>Civil Status</label>
          <input type="text" placeholder="Civil Status"onChange={e => setCivilStatus(e.target.value)} />
        </div>
        <div>
          <label>Address</label>
          <input type="text" placeholder="Address"onChange={e => setAddress(e.target.value)} />
        </div>
        <button type="submit">Save</button>
      </form>
    </div>
  );
}



