# 🌍 Interactive Energy Generation Explorer

An interactive web application for exploring and comparing energy generation data across countries and energy sources.

## 🚀 Features

* **Interactive Country Selection**: Choose from 200+ countries worldwide
* **Multiple Energy Sources**: Compare Solar, Nuclear, Coal, Gas, Wind, Hydro, and more
* **Date Range Filtering**: Select custom time periods for analysis
* **Real-time Plot Updates**: Dynamic charts that update as you make selections
* **Hover Information**: Detailed tooltips showing exact values and dates
* **Data Export**: View and download raw data tables
* **Global Statistics**: Quick insights into energy trends worldwide

## 📊 Data Source

This app uses data from Ember Energy, which provides comprehensive monthly electricity generation data for countries worldwide.

## 🛠️ Installation

### Prerequisites

* Python 3.7 or higher
* pip (Python package installer)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/literato1987/energy-app.git
cd energy-app
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run energy_app.py
```

4. **Open your browser**
The app will automatically open at `http://localhost:8501`

## 🎯 How to Use

### Selecting Countries

1. Look for the "🌍 Countries" section in the sidebar
2. Click on the dropdown to see all available countries
3. Select multiple countries by clicking on them
4. The plot will update automatically

### Choosing Energy Sources

1. Find the "⚡ Energy Sources" section
2. Select energy sources like Solar, Nuclear, Coal, etc.
3. You can compare multiple sources simultaneously

### Setting Date Range

1. Use the "📅 Date Range" selector
2. Choose your start and end dates
3. The data will filter to show only that period

### Interactive Features

* **Hover over lines** to see exact values
* **Click legend items** to show/hide specific data series
* **Zoom and pan** the chart for detailed exploration
* **Download the plot** as an image

## 📈 Example Use Cases

### Compare Renewable Energy Adoption

* Select countries: Germany, Denmark, Spain
* Choose sources: Solar, Wind
* See how different countries transition to renewables

### Nuclear Energy Comparison

* Select countries: France, USA, China
* Choose source: Nuclear
* Compare nuclear energy policies and trends

### Fossil Fuel Dependence

* Select countries: China, USA, India
* Choose sources: Coal, Gas
* Analyze fossil fuel usage patterns

## 🏗️ Project Structure

```
energy-app/
├── energy_app.py          # Main Streamlit application
├── requirements.txt       # Python dependencies
└── README.md            # This file
```

## 🛠️ Development

### Adding New Features

1. **Fork the repository**
2. **Create a feature branch**
```bash
git checkout -b feature/new-feature
```
3. **Make your changes**
4. **Test the application**
```bash
streamlit run energy_app.py
```
5. **Commit and push**
```bash
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```
6. **Create a Pull Request**

### Local Development

For development, you can run the app with auto-reload:
```bash
streamlit run energy_app.py --server.runOnSave true
```

## 📊 Data Schema

The application uses the following data structure:

| Column   | Description                                |
| -------- | ------------------------------------------ |
| Area     | Country name                               |
| Variable | Energy source (Solar, Nuclear, Coal, etc.) |
| Date     | Monthly date                               |
| Value    | Generation in TWh                          |
| Unit     | Unit of measurement (TWh)                  |

## 🤝 Contributing

We welcome contributions! Please feel free to:

* 🐛 Report bugs
* 💡 Suggest new features
* 📝 Improve documentation
* 🔧 Submit code improvements

### Contributing Guidelines

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Ensure the app runs without errors
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

* Data provided by Ember Energy
* Built with Streamlit
* Charts powered by Plotly

## 📞 Support

If you have questions or need help:

* 📧 Open an issue on GitHub
* 🐛 Report bugs with detailed descriptions
* 💡 Suggest features with use cases

---

**Made with ❤️ for energy data exploration** 