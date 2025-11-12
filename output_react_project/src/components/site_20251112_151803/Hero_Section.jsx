
import React, { useState } from 'react';

const HeroSection = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const navLinks = [
    { href: '#gallery', label: 'Gallery' },
    { href: '#missions', label: 'Missions' },
    { href: '#about', label: 'About Us' },
    { href: '#contact', label: 'Contact' },
  ];

  return (
    <div className="relative bg-gray-900 min-h-screen flex flex-col items-center justify-center overflow-hidden">
      {/* Background Image */}
      <div
        className="absolute inset-0 w-full h-full bg-cover bg-center bg-fixed"
        style={{ backgroundImage: "url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop')" }}
      ></div>
      {/* Overlay */}
      <div className="absolute inset-0 w-full h-full bg-black opacity-60"></div>

      {/* Header */}
      <header className="absolute top-0 left-0 right-0 z-20">
        <div className="max-w-7xl mx-auto px-6 lg:px-8">
          <div className="flex justify-between items-center py-6">
            {/* Logo */}
            <a href="#" className="text-2xl font-bold text-pink-500 tracking-wider">
              StellarScapes
            </a>

            {/* Desktop Navigation */}
            <nav className="hidden md:flex space-x-8">
              {navLinks.map((link) => (
                <a key={link.href} href={link.href} className="text-gray-100 hover:text-pink-500 transition-colors duration-300">
                  {link.label}
                </a>
              ))}
            </nav>

            {/* Mobile Menu Button */}
            <div className="md:hidden">
              <button onClick={() => setIsMenuOpen(!isMenuOpen)} className="text-gray-100 focus:outline-none">
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d={isMenuOpen ? "M6 18L18 6M6 6l12 12" : "M4 6h16M4 12h16m-7 6h7"}></path>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Mobile Menu */}
      {isMenuOpen && (
        <div className="md:hidden absolute top-0 left-0 w-full h-screen bg-gray-900/95 z-10 flex flex-col items-center justify-center">
          <nav className="flex flex-col items-center space-y-8">
            {navLinks.map((link) => (
              <a key={link.href} href={link.href} onClick={() => setIsMenuOpen(false)} className="text-gray-100 text-2xl hover:text-pink-500 transition-colors duration-300">
                {link.label}
              </a>
            ))}
          </nav>
        </div>
      )}

      {/* Hero Content */}
      <div className="relative z-10 flex-1 flex items-center text-center">
        <div className="max-w-7xl mx-auto px-6 lg:px-8">
          <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold text-white leading-tight tracking-wide" style={{ textShadow: '0 2px 4px rgba(0,0,0,0.5)' }}>
            Explore the Cosmos
          </h1>
          <p className="mt-6 text-lg md:text-xl max-w-3xl mx-auto text-gray-200 leading-relaxed" style={{ textShadow: '0 1px 3px rgba(0,0,0,0.5)' }}>
            Journey through breathtaking galaxies, nebulae, and star systems. Your adventure into the infinite expanse of the universe begins now.
          </p>
          <a
            href="#missions"
            className="mt-10 inline-block bg-pink-500 text-white font-semibold px-8 py-3 rounded-lg shadow-lg hover:bg-pink-600 transition-all duration-300 transform hover:scale-105"
          >
            Begin Your Voyage
          </a>
        </div>
      </div>
    </div>
  );
};

export default HeroSection;
