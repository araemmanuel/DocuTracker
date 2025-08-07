'use client';

import { usePathname } from 'next/navigation';
import Link from 'next/link';
import LogoutButton from './LogoutButton'; // Adjust if different location

export default function RootLayoutContent({ children }) {
  const pathname = usePathname();
  const isLoginPage = pathname === '/login';

  if (isLoginPage) {
    return <>{children}</>;
  }

  return (
    <div className="layout-container">
      <aside className="sidebar">
        <div className="logo">AICS-IMS</div>
        <nav className="nav-links">
          <Link href="/dashboard">🏠 Dashboard</Link>
          <Link href="/beneficiary">🧍 Beneficiary</Link>
          <Link href="/claimant">👥 Claimant</Link>
          <Link href="/application">📄 Application</Link>
          <Link href="/report">📁 Report</Link>
        </nav>
      </aside>
      <main className="content">
        <div className="top-bar">
          <div className="top-icons">
            <span>🔍</span>
            <LogoutButton />
          </div>
        </div>
        <div className="main-card">{children}</div>
      </main>
    </div>
  );
}
