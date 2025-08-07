// app/layout.js
import './globals.css';
import RootLayoutContent from '../components/RootLayoutContent';

export const metadata = {
  title: 'AICS-IMS',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <RootLayoutContent>{children}</RootLayoutContent>
      </body>
    </html>
  );
}
