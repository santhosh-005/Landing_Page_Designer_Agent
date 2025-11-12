import React from 'react';

const Footer = () => {
  const socialLinks = [
    {
      label: 'Twitter',
      href: '#',
      icon: (
        <svg
          className="w-6 h-6"
          fill="currentColor"
          viewBox="0 0 24 24"
          aria-hidden="true"
        >
          <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" />
        </svg>
      ),
    },
    {
      label: 'Instagram',
      href: '#',
      icon: (
        <svg
          className="w-6 h-6"
          fill="currentColor"
          viewBox="0 0 24 24"
          aria-hidden="true"
        >
          <path
            fillRule="evenodd"
            d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.024.06 1.378.06 3.808s-.012 2.784-.06 3.808c-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.024.048-1.378.06-3.808.06s-2.784-.012-3.808-.06c-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.048-1.024-.06-1.378-.06-3.808s.012-2.784.06-3.808c.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 016.345 2.525c.636-.247 1.363-.416 2.427-.465C9.792 2.013 10.146 2 12.573 2h-.258zM12 4.837a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 15.318a3.318 3.318 0 110-6.636 3.318 3.318 0 010 6.636z"
            clipRule="evenodd"
          />
          <path d="M16.838 7.162a1.2 1.2 0 11-2.4 0 1.2 1.2 0 012.4 0z" />
        </svg>
      ),
    },
    {
      label: 'LinkedIn',
      href: '#',
      icon: (
        <svg
          className="w-6 h-6"
          fill="currentColor"
          viewBox="0 0 24 24"
          aria-hidden="true"
        >
          <path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.25 6.5 1.75 1.75 0 016.5 8.25zM19 19h-3v-4.75c0-1.4-.5-2-1.5-2s-1.5 1-1.5 2V19h-3v-9h3V11c1-2 2-2 3.5-2 2.5 0 4 1.5 4 4.5z" />
        </svg>
      ),
    },
  ];

  const navLinks = [
    { name: 'About', href: '#' },
    { name: 'Missions', href: '#' },
    { name: 'Gallery', href: '#' },
    { name: 'Contact', href: '#' },
  ];

  return (
    <footer className="bg-gray-100">
      <div className="max-w-7xl mx-auto py-16 px-6 lg:px-8">
        <div className="flex flex-col md:flex-row justify-between items-center space-y-8 md:space-y-0 text-center md:text-left">
          
          {/* Logo and Copyright */}
          <div>
            <a href="#" className="text-3xl font-bold text-gray-900 hover:text-blue-600 transition-colors duration-300">
              StellarVoyage
            </a>
            <p className="mt-2 text-sm text-gray-600">
              Exploring the cosmos, one star at a time.
            </p>
          </div>

          {/* Navigation Links */}
          <nav className="flex flex-wrap justify-center gap-x-6 gap-y-2" aria-label="Footer">
            {navLinks.map((link) => (
              <a 
                key={link.name} 
                href={link.href} 
                className="text-lg text-gray-900 hover:text-pink-500 transition-colors duration-300"
              >
                {link.name}
              </a>
            ))}
          </nav>

          {/* Social Media Icons */}
          <div className="flex justify-center space-x-6">
            {socialLinks.map((item) => (
              <a 
                key={item.label} 
                href={item.href} 
                className="text-gray-500 hover:text-pink-500 transition-colors duration-300"
              >
                <span className="sr-only">{item.label}</span>
                {item.icon}
              </a>
            ))}
          </div>
        </div>

        <div className="mt-12 pt-8 border-t border-gray-300 text-center text-sm text-gray-600">
          <p>&copy; {new Date().getFullYear()} StellarVoyage Inc. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
