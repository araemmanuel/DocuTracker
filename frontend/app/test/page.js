// pages/test.js or app/test/page.js (depending on your Next.js version)
'use client';

import { useState } from 'react';

export default function TestConnection() {
    const [response, setResponse] = useState(null);
    const [loading, setLoading] = useState(false);
  const API_URL = process.env.NEXT_PUBLIC_API_URL;

    const testConnection = async () => {
        setLoading(true);
        try {
            const res = await fetch(`${API_URL}/api/testcon/`);
            const data = await res.json();
            setResponse(data);
        } catch (error) {
            setResponse({ error: 'Connection failed: ' + error.message });
        }
        setLoading(false);
    };

    return (
        <div style={{ padding: '20px' }}>
            <h1>Test Django-Next.js Connections</h1>
            <button onClick={testConnection} disabled={loading}>
                {loading ? 'Testing...' : 'Test Connection'}
            </button>
            
            {response && (
                <div style={{ marginTop: '20px', padding: '10px', backgroundColor: '#f0f0f0' }}>
                    <pre>{JSON.stringify(response, null, 2)}</pre>
                </div>
            )}
        </div>
    );
}