# Shadcn Theme for Odoo 18

A modern, sleek Odoo theme inspired by the shadcn/ui design system. This theme brings a clean, professional look to your Odoo website with smooth animations and excellent user experience.

## Features

### 🎨 Modern Design
- Clean and minimalist interface
- Inspired by shadcn/ui design principles
- Professional color schemes
- Smooth transitions and animations

### 🎯 Key Components

#### Typography
- Inter font family for modern look
- Optimized font weights and sizes
- Excellent readability

#### Color System
- Carefully curated color palettes
- Zinc/Slate neutral colors
- Beautiful primary, success, warning, and danger colors
- Support for light and dark variations

#### UI Components
- Modern buttons with hover effects
- Elegant cards with smooth transitions
- Clean form inputs with focus states
- Professional badges and labels

#### Snippets
- **Hero Section**: Eye-catching landing section with call-to-action
- **Features Section**: Showcase your product features beautifully
- **Call to Action**: Convert visitors with compelling CTAs
- **Statistics**: Display impressive numbers and achievements

### 🚀 Performance
- Optimized CSS and JavaScript
- Smooth animations using CSS transitions
- Lightweight and fast loading

### 📱 Responsive Design
- Mobile-first approach
- Looks great on all devices
- Optimized for touch interactions

### 🛠️ Easy Customization
- Well-organized SCSS structure
- Easy color customization
- Flexible snippet options
- Website builder compatible

## Installation

1. Download the theme module
2. Place it in your Odoo addons directory
3. Update the app list in Odoo
4. Install "Shadcn Theme" from Apps menu
5. Activate the theme from Website > Configuration > Settings

## Usage

### Customizing Colors

Edit `/static/src/scss/primary_variables.scss` to customize the color palette:

```scss
$o-color-palettes: (
    'primary': (
        '500': #0ea5e9,  // Change this to your brand color
        // ...
    ),
);
```

### Using Snippets

1. Go to your website in edit mode
2. Click "Blocks" to see available snippets
3. Drag and drop Shadcn snippets onto your page:
   - Shadcn Hero Section
   - Shadcn Features Section
   - Shadcn Call to Action
   - Shadcn Statistics

### Customizing Header and Footer

The theme includes custom header and footer templates:
- Enable them from Website > Configuration > Menu Editor
- Customize content directly in the XML files

## Design Principles

This theme follows shadcn/ui design principles:
- **Simplicity**: Clean, uncluttered interfaces
- **Consistency**: Uniform design language throughout
- **Accessibility**: High contrast, readable typography
- **Modern**: Contemporary design trends
- **Flexible**: Easy to customize and extend

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Credits

- Inspired by [shadcn/ui](https://ui.shadcn.com/)
- Built for Odoo 18
- Uses Inter font family from Google Fonts

## License

LGPL-3

## Support

For issues, questions, or contributions, please visit:
https://github.com/lati-tibabu/miniature-octo-memory

## Version History

### 1.0.0 (2024)
- Initial release
- Modern shadcn-inspired design
- Responsive layout
- Custom snippets
- Header and footer templates
- Full Odoo 18 compatibility
