import React from 'react';
import Hero_Section from './components/site_20251112_151803/Hero_Section.jsx';
import Cosmic_Wonders from './components/site_20251112_151803/Cosmic_Wonders.jsx';
import Stellar_Gallery from './components/site_20251112_151803/Stellar_Gallery.jsx';
import Join_Our_Voyage from './components/site_20251112_151803/Join_Our_Voyage.jsx';
import Footer from './components/site_20251112_151803/Footer.jsx';
import './index.css';

function App() {
  return (
    <div className="min-h-screen">
      <Hero_Section />
      <Cosmic_Wonders />
      <Stellar_Gallery />
      <Join_Our_Voyage />
      <Footer />
    </div>
  );
}

export default App;
