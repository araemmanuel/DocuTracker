'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import axios from 'axios'

export default function ClaimantForm() {
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
    const [occupation, setOccupation] = useState('')
    const [relationship_to_beneficiary, setBeneRel] = useState('')
    const [salary, setSalary] = useState('')
    const API_URL = process.env.NEXT_PUBLIC_API_URL;
    
  return (
    <div>
      <h2 className="text-2xl font-bold mb-6 text-green-900">Claimant Form</h2>
      <form className="space-y-4">
        <div>
          <label>Full Name</label>
          <input type="text" placeholder="Full Name" />
        </div>
        <div>
          <label>Birthday</label>
          <input type="text" placeholder="Birthday" />
        </div>
        <div>
          <label>Age</label>
          <input type="text" placeholder="Age" />
        </div>
        <div>
          <label>Contact Number</label>
          <input type="text" placeholder="Contact Number"/>
        </div>
        <div>
          <label>Gender</label>
          <input type="text" placeholder="Gender"/>
        </div>
        <div>
          <label>Educational Attainment</label>
          <input type="text" placeholder="Educational Attainment"/>
        </div>
        <div>
          <label>Civil Status</label>
          <input type="text" placeholder="Civil Status"/>
        </div>
        <div>
          <label>Address</label>
          <input type="text" placeholder="Address"/>
        </div>
        <div>
          <label>Occupation</label>
          <input type="text" placeholder="Occupation"/>
        </div>
        <div>
          <label>Relationship to Beneficiary</label>
          <input type="text" placeholder="Relationship to Beneficiary"/>
        </div>
        <div>
          <label>Salary</label>
          <input type="text" placeholder="Salary"/>
        </div>
        <div>
          <label>Client's category</label>
          <input type="text" placeholder="Client's category"/>
        </div>
        <div>
          <label>Beneficiary's Category</label>
          <input type="text" placeholder="Beneficiary's Category"/>
        </div>
        <div>
          <label>Assistance Availed</label>
          <input type="text" placeholder="Assistance Availed"/>
        </div>
        <div>
          <label>Recommended Services / Assistance</label>
          <input type="text" placeholder="Recommended Services / Assistance"/>
        </div>
        <div>
          <label>Problems presented</label>
          <input type="text" placeholder="Problems presented"/>
        </div>
        <div>
          <label>Social Worker's Assessment</label>
          <input type="text" placeholder="Social Worker's Assessment"/>
        </div>
        <button type="submit">Save</button>
        <button>Print</button>
      </form>
    </div>
  );
}
