'use client';

import { useRouter } from 'next/navigation';
import { useEffect } from 'react';

export default function LogoutButton() {
  const router = useRouter();

  const handleLogout = () => {
    // Clear JWT tokens
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')

    // Clear axios auth header if you're using it globally
    if (typeof window !== 'undefined') {
      delete window.axios?.defaults?.headers?.common['Authorization']
    }
    router.push('/login');
  };

  return (
    <button className="profile-icon" title="Logout" onClick={handleLogout}>
      👤
    </button>
  );
}
