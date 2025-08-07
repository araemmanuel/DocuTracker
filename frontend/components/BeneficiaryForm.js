'use client';
import styles from '../styles/dashboard.module.css';

export default function BeneficiaryForm() {
  return (
    <div className={styles.formContainer}>
      <h2 className={styles.title}>Beneficiary Form</h2>
      <form className={styles.form}>
        <input type="text" placeholder="Full Name" />
        <input type="text" placeholder="Birthday" />
        <input type="text" placeholder="Age" />
        <input type="text" placeholder="Contact Number"/>
        <input type="text" placeholder="Gender"/>
        <input type="text" placeholder="Educational Attainment"/>
        <input type="text" placeholder="Civil Status"/>
        <input type="text" placeholder="Address"/>
        <input type="file" />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}
