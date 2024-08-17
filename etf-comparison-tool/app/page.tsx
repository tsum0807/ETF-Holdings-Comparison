import React from 'react';

const LandingPage: React.FC = () => {
  return (
    <div style={{ fontFamily: 'Arial, sans-serif', color: '#333' }}>
      {/* Hero Section */}
      <section style={{
        background: 'linear-gradient(135deg, #0066cc, #00cc99)',
        color: '#fff',
        textAlign: 'center',
        padding: '100px 20px',
        height: '100vh',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center'
      }}>
        <h1 style={{ fontSize: '4rem', margin: '0' }}>ETF Comparison Tool</h1>
        <p style={{ fontSize: '1.5rem', margin: '20px 0' }}>
          Compare ETF holdings and find overlaps with ease. Make informed investment decisions today!
        </p>
        <a href="#features" style={{
          textDecoration: 'none',
          color: '#fff',
          background: '#ff6600',
          padding: '15px 30px',
          borderRadius: '5px',
          fontSize: '1rem',
          fontWeight: 'bold',
        }}>Get Started</a>
      </section>

      {/* Features Section */}
      <section id="features" style={{ padding: '50px 20px', textAlign: 'center' }}>
        <h2 style={{ fontSize: '2.5rem', margin: '0 0 20px' }}>Features</h2>
        <div style={{
          display: 'flex',
          flexDirection: 'row',
          justifyContent: 'center',
          gap: '20px',
          flexWrap: 'wrap'
        }}>
          <div style={{
            flex: '1 1 300px',
            background: '#f4f4f4',
            padding: '20px',
            borderRadius: '10px',
            boxShadow: '0 4px 8px rgba(0,0,0,0.1)'
          }}>
            <h3>Comprehensive Comparisons</h3>
            <p>Get detailed insights into ETF holdings and identify overlaps across different funds.</p>
          </div>
          <div style={{
            flex: '1 1 300px',
            background: '#f4f4f4',
            padding: '20px',
            borderRadius: '10px',
            boxShadow: '0 4px 8px rgba(0,0,0,0.1)'
          }}>
            <h3>Easy-to-Use Interface</h3>
            <p>Our intuitive interface makes it simple to perform in-depth comparisons with just a few clicks.</p>
          </div>
          <div style={{
            flex: '1 1 300px',
            background: '#f4f4f4',
            padding: '20px',
            borderRadius: '10px',
            boxShadow: '0 4px 8px rgba(0,0,0,0.1)'
          }}>
            <h3>Real-Time Data</h3>
            <p>Access up-to-date information to ensure your investment decisions are based on the latest data.</p>
          </div>
        </div>
      </section>

      {/* Call-to-Action Section */}
      <section style={{
        background: '#333',
        color: '#fff',
        padding: '50px 20px',
        textAlign: 'center'
      }}>
        <h2 style={{ fontSize: '2.5rem', margin: '0 0 20px' }}>[WIP] Ready to Keep Track of Your Comparisons?</h2>
        <p style={{ fontSize: '1.2rem', margin: '0 0 20px' }}>
          Create an account now to save your comparisons and access them anytime, anywhere.
        </p>
        <a href="#signup" style={{
          textDecoration: 'none',
          color: '#fff',
          background: '#ff6600',
          padding: '15px 30px',
          borderRadius: '5px',
          fontSize: '1rem',
          fontWeight: 'bold',
          margin: '10px'
        }}>Sign Up</a>
        <p style={{ margin: '20px 0 0' }}>
          <a href="/about" style={{
            textDecoration: 'none',
            color: '#ff6600',
            fontSize: '1rem',
            fontWeight: 'bold'
          }}>Learn More About Us</a>
        </p>
      </section>

    </div>
  );
};

export default LandingPage;
