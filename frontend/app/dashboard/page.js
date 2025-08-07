// 'use client'

// import { useEffect } from 'react'
// import { useRouter } from 'next/navigation'
// import Link from 'next/link';
// import LogoutButton from '@/components/LogoutButton';
// import styles from './dashboard.module.css';


// export default function Dashboard() {
//   const router = useRouter()

//   useEffect(() => {
//     const token = localStorage.getItem('access_token')
//     if (!token) {
//       router.push('/login')
//     }
//   }, [])

//   return (
//     // <div>
//     //   <h1>Dashboard</h1>
//     //   <p>You are logged in!</p>
//     //   <LogoutButton />
//     // </div>
//     <div className={styles.layout}>
//       <aside className={styles.sidebar}>
//         <h2 className={styles.logo}>AICS-IMS</h2>
//         <nav className={styles.nav}>
//           <a href="/" className={styles.navItem}>
//             🏠 Dashboard
//           </a>
//           <a href="/beneficiary" className={styles.navItem}>
//             👤 Beneficiary
//           </a>
//           <a href="/claimant" className={styles.navItem}>
//             👥 Claimant
//           </a>
//           <a href="/application" className={`${styles.navItem} ${styles.active}`}>
//             📄 Application
//           </a>
//           <a href="/report" className={styles.navItem}>
//             📊 Report
//           </a>
//         </nav>
//       </aside>

//       <main className={styles.main}>
//         <div className={styles.topbar}>
//           <button className={styles.iconBtn}>🔍</button>
//           <button className={styles.iconBtn}>👤</button>
//         </div>

//         <div className={styles.formContainer}>
//           <h1 className={styles.title}>Application Form</h1>
//           <form className={styles.form}>
//             <label>Full Name</label>
//             <input type="text" required />

//             <label>Email</label>
//             <input type="email" required />

//             <label>Phone</label>
//             <input type="tel" required />

//             <label>Upload Document</label>
//             <input type="file" />

//             <button type="submit">Submit</button>
//           </form>
//         </div>
//       </main>
//     </div>
//   )
// }
export default function DashboardHome() {
  return (
    <div>
      <h2 className="text-2xl font-bold mb-6 text-green-900">Dashboard Form</h2>
      {/* Add form fields here */}
    </div>
  );
}