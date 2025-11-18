# miniature-octo-memory

## Shadcn Theme for Odoo 18

A modern, sleek Odoo 18 theme inspired by the shadcn/ui design system.

### Features

- 🎨 **Modern Design**: Clean, minimalist interface inspired by shadcn/ui
- 🚀 **Fast & Responsive**: Lightning-fast performance with mobile-first design
- 🎯 **Easy to Use**: Simple installation and configuration
- 🛠️ **Customizable**: Easy color and style customization
- 📦 **Snippet Library**: Pre-built components for quick page building

### Installation

1. Clone this repository or download the `theme_shadcn` folder
2. Copy the `theme_shadcn` folder to your Odoo addons directory
3. Restart your Odoo server
4. Go to Apps menu and update the apps list
5. Search for "Shadcn Theme" and click Install
6. Activate the theme from Website > Configuration > Settings

### What's Included

- **Custom Header & Footer**: Modern, clean navigation and footer layouts
- **Color System**: Carefully curated color palettes (Zinc, Slate, Blue, Green)
- **Typography**: Inter font family for modern, readable text
- **UI Components**: Buttons, cards, forms, badges with shadcn-inspired styling
- **Website Snippets**:
  - Hero Section: Eye-catching landing sections
  - Features Grid: Showcase product features
  - Call to Action: Conversion-optimized CTAs
  - Statistics: Display metrics and achievements

### Theme Structure

```
theme_shadcn/
├── __init__.py
├── __manifest__.py
├── README.md
├── static/
│   ├── description/       # Theme metadata and images
│   └── src/
│       ├── scss/          # Stylesheets
│       ├── js/            # JavaScript files
│       └── img/           # Images and icons
└── views/
    ├── assets.xml         # Asset definitions and templates
    ├── snippets.xml       # Website builder snippets
    └── options.xml        # Customization options
```

### Customization

#### Changing Colors

Edit `theme_shadcn/static/src/scss/primary_variables.scss` to customize colors:

```scss
$o-color-palettes: (
    'primary': (
        '500': #0ea5e9,  // Change to your brand color
    ),
);
```

#### Adding Custom Snippets

Add new snippets in `theme_shadcn/views/snippets.xml` following the existing pattern.

### Design Philosophy

This theme follows the shadcn/ui design principles:

- **Simplicity First**: Clean, uncluttered interfaces
- **Consistency**: Uniform design language
- **Accessibility**: High contrast, readable typography
- **Modern Aesthetics**: Contemporary design trends
- **Flexibility**: Easy to customize and extend

### Browser Support

- Chrome (latest)
- Firefox (latest)  
- Safari (latest)
- Edge (latest)
- Mobile browsers

### Credits

- Inspired by [shadcn/ui](https://ui.shadcn.com/)
- Built for Odoo 18
- Uses Inter font from Google Fonts

### License

LGPL-3

### Support

For issues or questions, please open an issue on GitHub.