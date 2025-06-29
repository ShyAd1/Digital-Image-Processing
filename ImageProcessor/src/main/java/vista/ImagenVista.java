/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package vista;


import java.awt.Color;
import java.awt.Graphics;
import java.awt.GridLayout;
import java.awt.image.BufferedImage;
import javax.swing.*;

public class ImagenVista extends javax.swing.JFrame {

    /**
     * Creates new form ImagenVista
     */
    public ImagenVista() {
        initComponents();
        this.setTitle("Procesamiento de Imágenes en Java");
    }
    
    // Métodos para acceder a los componentes
    public JSlider getBrightnessSlider() {
        return brightnessSlider;
    }

    public JSlider getContrastSlider() {
        return contrastSlider;
    }

    public JLabel getImageLabel() {
        return imageLabel;
    }

    public JButton getLoadButton() {
        return loadButton;
    }

    public JButton getSaveButton() {
        return saveButton;
    }

    public JButton getResetButton() {
        return resetButton;
    }

    public JButton getGrayButton() {
        return grayButton;
    }

    public JButton getRedButton() {
        return redButton;
    }

    public JButton getGreenButton() {
        return greenButton;
    }

    public JButton getBlueButton() {
        return blueButton;
    }

    public JButton getYiqButton1() {
        return yiqButton1;
    }

    public JButton getYiqToRGBButton() {
        return yiqToRGBButton;
    }

    public JButton getHsiButton1() {
        return hsiButton1;
    }

    public JButton getHsiToRGBButton() {
        return hsiToRGBButton;
    }

    public JButton getHsvButton1() {
        return hsvButton1;
    }

    public JButton getHsvToRGBButton() {
        return hsvToRGBButton;
    }

    public JButton getRgbToCMYButton() {
        return rgbToCMYButton;
    }

    public JButton getCmyToRGBButton() {
        return cmyToRGBButton;
    }

    public JButton getCmyToCMYKButton() {
        return cmyToCMYKButton;
    }

    public JButton getRgbToHSIButton() {
        return rgbToHSIButton;
    }

    public JButton getRgbToHSVButton() {
        return rgbToHSVButton;
    }

    public JButton getRgbToLabButton() {
        return rgbToLabButton;
    }

    public JButton getLabToRGBButton() {
        return labToRGBButton;
    }
    
    public JButton getCannyEdgeButton() {
        return cannyEdgeButton;
    }

    public JButton getRgbToYIQButton() {
        return rgbToYIQButton;
    }

    public JButton getShowHistogramButton() {
        return showHistogramButton;
    }

    public JButton getScaleHistogramButton() {
        return scaleHistogramButton;
    }

    public JButton getShiftHistogramButton() {
        return shiftHistogramButton;
    }

    public JButton getMatchHistogramButton() {
        return matchHistogramButton;
    }

    public JButton getEqualizeHistogramButton() {
        return equalizeHistogramButton;
    }

    public JButton getEqualizeUniformButton() {
        return equalizeUniformButton;
    }

    public JButton getEqualizeExponentialButton() {
        return equalizeExponentialButton;
    }

    public JButton getEqualizeRayleighButton() {
        return equalizeRayleighButton;
    }

    public JButton getEqualizeHyperbolicLogarithmicButton() {
        return equalizeHyperbolicLogarithmicButton;
    }

    public JButton getEqualizeHyperbolicRootsButton() {
        return equalizeHyperbolicRootsButton;
    }

    public JButton getBinarization1Button() {
        return binarization1Button;
    }

    public JButton getBinarization2Button() {
        return binarization2Button;
    }

    public JButton getBinarization3Button() {
        return binarization3Button;
    }

    public JButton getBinarizationToRGBButton() {
        return binarizationToRGBButton;
    }

    public JButton getInvertBinButton() {
        return invertBinButton;
    }

    public JButton getSumButton() {
        return sumButton;
    }

    public JButton getSubtractionButton() {
        return subtractionButton;
    }

    public JButton getMultiplicationButton() {
        return multiplicationButton;
    }

    public JButton getDivisionButton() {
        return divisionButton;
    }

    public JButton getEqualButton() {
        return equalButton;
    }

    public JButton getNotEqualButton() {
        return notEqualButton;
    }

    public JButton getGreaterThanButton() {
        return greaterThanButton;
    }

    public JButton getGreaterThanOrEqualButton() {
        return greaterThanOrEqualButton;
    }

    public JButton getLessThanButton() {
        return lessThanButton;
    }

    public JButton getLessThanOrEqualButton() {
        return lessThanOrEqualButton;
    }

    public JButton getAndButton() {
        return andButton;
    }

    public JButton getOrButton() {
        return orButton;
    }

    public JButton getXorButton() {
        return xorButton;
    }

    public JButton getNotButton() {
        return notButton;
    }

    public JButton getTranslationButton() {
        return translationButton;
    }

    public JButton getRotationButton() {
        return rotationButton;
    }

    public JButton getInterpolationButton() {
        return interpolationButton;
    }

    public JButton getGaussianNoiseButton() {
        return gaussianNoiseButton;
    }

    public JButton getUniformNoiseButton() {
        return uniformNoiseButton;
    }

    public JButton getExponentialNoiseButton() {
        return exponentialNoiseButton;
    }

    public JButton getGammaNoiseButton() {
        return gammaNoiseButton;
    }

    public JButton getRayleighNoiseButton() {
        return rayleighNoiseButton;
    }

    public JButton getSaltPepperNoiseButton() {
        return saltPepperNoiseButton;
    }

    public JButton getSaltNoiseButton() {
        return saltNoiseButton;
    }

    public JButton getPepperNoiseButton() {
        return pepperNoiseButton;
    }

    public JButton getCoherentNoiseButton() {
        return coherentNoiseButton;
    }
    
    public JButton getHomogeneityOperatorButton() {
        return homogeneityOperatorButton;
    }
    
    public JButton getDifferenceOperatorButton() {
        return differenceOperatorButton;
    }
    
    public JButton getGradientFirstOrderButton() {
        return gradientFirstOrderButton;
    }
    
    public JButton getPrewittButton() {
        return prewittButton;
    }
    
    public JButton getSobelButton() {
        return sobelButton;
    }
    
    public JButton getFreiChenButton() {
        return freiChenButton;
    }
    
    public JButton getCompassGradientButton() {
        return compassGradientButton;
    }
    
    public JButton getLaplacianButton() {
        return laplacianButton;
    }
    
    public JButton getPrewittSecondOrderButton() {
        return prewittSecondOrderButton;
    }
    
    public JButton getKirschButton() {
        return kirschButton;
    }
    
    public JButton getRobinsonButton() {
        return notButton1;
    }
    
    public JButton getAverageFilterButton() {
        return lessThanButton1;
    }
    
    public JButton getGaussianFilterButton() {
        return lessThanOrEqualButton1;
    }
    
    public JButton getSharpenFilterButton() {
        return greaterThanButton1;
    }

    public JButton getMedianFilterButton() {
        return minFilterButton;
    }

    public JButton getMinFilterButton() {
        return minFilterButton;
    }
    
    public JButton getMaxFilterButton() {
        return maxFilterButton;
    }
    
    public JButton getMidpointFilterButton() {
        return midpointFilterButton;
    }
    
    public JButton getAlphaTrimmedFilterButton() {
        return alphaTrimmedFilterButton;
    }

    public JButton getHarmonicMeanFilterButton() {
        return harmonicMeanFilterButton;
    }
    
    public JButton getContraHarmonicFilterButton() {
        return contraHarmonicFilterButton;
    }
    
    public JButton getGeometricMeanFilterButton() {
        return geometricMeanFilterButton;
    }
    
    public JButton getMaxMinFilterButton() {
        return maxMinFilterButton;
    }
    
    public JButton getArithmeticMeanFilterButton() {
        return arithmeticMeanFilterButton;
    }
    
    public JButton getContraGeometricMeanFilterButton() {
        return contraGeometricMeanFilterButton;
    }
    
    public JButton getModeFilterButton() {
        return modeFilterButton;
    }
    
    public JButton getCompararFiltrosButton() {
        return compararFiltrosButton;
    }

    public JButton getBinaryErotionButton() {
        return BinaryErotionButton;
    }

    public JButton getBinaryDilationButton() {
        return BinaryDilationButton;
    }

    public JButton getGrayScaleErotionButton() {
        return GrayScaleErotionButton;
    }

    public JButton getGrayScaleDilationButton() {
        return GrayScaleDilationButton;
    }

    public JButton getBinaryClosingButton() {
        return BinaryClosingButton;
    }

    public JButton getBinaryOpeningButton() {
        return BinaryOpeningButton;
    }

    public JButton getGrayScaleClosingButton() {
        return GrayScaleClosingButton;
    }

    public JButton getGrayScaleOpeningButton() {
        return GrayScaleOpeningButton;
    }
    
    

    // Método para actualizar la imagen en el JLabel
    public void mostrarImagen(BufferedImage imagen) {
        if (imagen == null) {
            imageLabel.setIcon(null);
        } else {
            ImageIcon icono = new ImageIcon(imagen);
            imageLabel.setIcon(icono);
        }
        imageLabel.repaint();
    }

    // Método para mostrar mensajes de error
    public void mostrarMensajeError(String mensaje) {
        JOptionPane.showMessageDialog(this, mensaje, "Error", JOptionPane.ERROR_MESSAGE);
    }
    
    // Método para mostrar los histogramas
    public void showHistogram(int[][] histogramRGB, int[] histogramGray, String title) {
        JFrame histogramFrame = new JFrame(title);
        histogramFrame.setSize(600, 400);
        histogramFrame.setLayout(new GridLayout(1, 2));

        JPanel rgbPanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                drawRGBHistogram(g, histogramRGB, getWidth(), getHeight());
            }
        };

        JPanel grayPanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                drawGrayHistogram(g, histogramGray, getWidth(), getHeight());
            }
        };

        histogramFrame.add(rgbPanel);
        histogramFrame.add(grayPanel);
        histogramFrame.setVisible(true);
    }
    
    // Dibuja el histograma de escala de grises
    private void drawGrayHistogram(Graphics g, int[] histogram, int width, int height) {
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, width, height);
        g.setColor(Color.BLACK);

        int max = 1;
        for (int value : histogram) {
            max = Math.max(max, value);
        }

        for (int i = 0; i < 256; i++) {
            int barHeight = (int) ((histogram[i] / (double) max) * (height - 20));
            g.setColor(Color.GRAY);
            g.fillRect(i * (width / 256), height - barHeight, width / 256, barHeight);
        }
    }

    // Dibuja los histogramas de los canales RGB
    private void drawRGBHistogram(Graphics g, int[][] histogram, int width, int height) {
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, width, height);

        int max = 1;
        for (int i = 0; i < 256; i++) {
            max = Math.max(max, Math.max(histogram[0][i], Math.max(histogram[1][i], histogram[2][i])));
        }

        for (int i = 0; i < 256; i++) {
            int barHeightR = (int) ((histogram[0][i] / (double) max) * (height - 20));
            int barHeightG = (int) ((histogram[1][i] / (double) max) * (height - 20));
            int barHeightB = (int) ((histogram[2][i] / (double) max) * (height - 20));

            g.setColor(Color.RED);
            g.fillRect(i * (width / 256), height - barHeightR, width / 256, barHeightR);
            g.setColor(Color.GREEN);
            g.fillRect(i * (width / 256), height - barHeightG, width / 256, barHeightG);
            g.setColor(Color.BLUE);
            g.fillRect(i * (width / 256), height - barHeightB, width / 256, barHeightB);
        }
    }

    // Métodos para solicitar valores al usuario
    public Integer solicitarUmbral(String mensaje) {
        String input = JOptionPane.showInputDialog(this, mensaje, "Ingrese Umbral", JOptionPane.QUESTION_MESSAGE);
        if (input == null) return null; // Si el usuario cancela
        try {
            int umbral = Integer.parseInt(input);
            if (umbral < 0 || umbral > 255) {
                mostrarMensajeError("El umbral debe estar entre 0 y 255.");
                return null;
            }
            return umbral;
        } catch (NumberFormatException e) {
            mostrarMensajeError("Por favor, ingrese un número válido.");
            return null;
        }
    }

    public Integer[] solicitarDosUmbrales(String mensaje1, String mensaje2) {
        Integer umbral1 = solicitarUmbral(mensaje1);
        if (umbral1 == null) return null;

        Integer umbral2 = solicitarUmbral(mensaje2);
        if (umbral2 == null) return null;

        if (umbral1 >= umbral2) {
            mostrarMensajeError("El umbral inferior debe ser menor que el superior.");
            return null;
        }

        return new Integer[]{umbral1, umbral2};
    }

    public Integer[] solicitarTresUmbrales(String mensaje1, String mensaje2, String mensaje3) {
        Integer umbral1 = solicitarUmbral(mensaje1);
        if (umbral1 == null) return null;

        Integer umbral2 = solicitarUmbral(mensaje2);
        if (umbral2 == null) return null;

        Integer umbral3 = solicitarUmbral(mensaje3);
        if (umbral3 == null) return null;

        if (umbral1 >= umbral2 || umbral2 >= umbral3) {
            mostrarMensajeError("Los umbrales deben estar en orden ascendente (umbral1 < umbral2 < umbral3).");
            return null;
        }

        return new Integer[]{umbral1, umbral2, umbral3};
    }

    public Double solicitarDouble(String mensaje) {
        String input = JOptionPane.showInputDialog(this, mensaje, "Ingrese Valor", JOptionPane.QUESTION_MESSAGE);
        if (input == null) return null; // Si el usuario cancela
        try {
            double valor = Double.parseDouble(input);
            if (valor <= 0) {
                mostrarMensajeError("El valor debe ser mayor que 0.");
                return null;
            }
            return valor;
        } catch (NumberFormatException e) {
            mostrarMensajeError("Por favor, ingrese un número válido.");
            return null;
        }
    }

    public Integer solicitarEntero(String mensaje) {
        String input = JOptionPane.showInputDialog(this, mensaje, "Ingrese Valor", JOptionPane.QUESTION_MESSAGE);
        if (input == null) return null; // Si el usuario cancela
        try {
            return Integer.parseInt(input);
        } catch (NumberFormatException e) {
            mostrarMensajeError("Por favor, ingrese un número entero válido.");
            return null;
        }
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        topPanel = new javax.swing.JPanel();
        loadButton = new javax.swing.JButton();
        saveButton = new javax.swing.JButton();
        resetButton = new javax.swing.JButton();
        leftPanel = new javax.swing.JPanel();
        sliderPanel1 = new javax.swing.JPanel();
        brightnessSlider = new javax.swing.JSlider();
        sliderPanel2 = new javax.swing.JPanel();
        contrastSlider = new javax.swing.JSlider();
        imageScrollPane = new javax.swing.JScrollPane();
        imageLabel = new javax.swing.JLabel();
        rightPanel = new javax.swing.JTabbedPane();
        filterPanel = new javax.swing.JPanel();
        grayButton = new javax.swing.JButton();
        redButton = new javax.swing.JButton();
        greenButton = new javax.swing.JButton();
        blueButton = new javax.swing.JButton();
        yiqButton1 = new javax.swing.JButton();
        hsvButton1 = new javax.swing.JButton();
        hsiButton1 = new javax.swing.JButton();
        cannyEdgeButton = new javax.swing.JButton();
        noisePanel = new javax.swing.JPanel();
        gaussianNoiseButton = new javax.swing.JButton();
        saltPepperNoiseButton = new javax.swing.JButton();
        uniformNoiseButton = new javax.swing.JButton();
        rayleighNoiseButton = new javax.swing.JButton();
        exponentialNoiseButton = new javax.swing.JButton();
        gammaNoiseButton = new javax.swing.JButton();
        coherentNoiseButton = new javax.swing.JButton();
        saltNoiseButton = new javax.swing.JButton();
        pepperNoiseButton = new javax.swing.JButton();
        conversionPanel = new javax.swing.JPanel();
        rgbToCMYButton = new javax.swing.JButton();
        cmyToRGBButton = new javax.swing.JButton();
        rgbToYIQButton = new javax.swing.JButton();
        yiqToRGBButton = new javax.swing.JButton();
        rgbToHSIButton = new javax.swing.JButton();
        hsiToRGBButton = new javax.swing.JButton();
        cmyToCMYKButton = new javax.swing.JButton();
        rgbToHSVButton = new javax.swing.JButton();
        hsvToRGBButton = new javax.swing.JButton();
        rgbToLabButton = new javax.swing.JButton();
        labToRGBButton = new javax.swing.JButton();
        binarizationPanel = new javax.swing.JPanel();
        binarization1Button = new javax.swing.JButton();
        binarization2Button = new javax.swing.JButton();
        binarization3Button = new javax.swing.JButton();
        invertBinButton = new javax.swing.JButton();
        binarizationToRGBButton = new javax.swing.JButton();
        operationPanel = new javax.swing.JPanel();
        translationButton = new javax.swing.JButton();
        rotationButton = new javax.swing.JButton();
        interpolationButton = new javax.swing.JButton();
        sumButton = new javax.swing.JButton();
        subtractionButton = new javax.swing.JButton();
        multiplicationButton = new javax.swing.JButton();
        divisionButton = new javax.swing.JButton();
        andButton = new javax.swing.JButton();
        orButton = new javax.swing.JButton();
        xorButton = new javax.swing.JButton();
        notButton = new javax.swing.JButton();
        lessThanButton = new javax.swing.JButton();
        lessThanOrEqualButton = new javax.swing.JButton();
        greaterThanButton = new javax.swing.JButton();
        greaterThanOrEqualButton = new javax.swing.JButton();
        equalButton = new javax.swing.JButton();
        notEqualButton = new javax.swing.JButton();
        modHistogramPanel = new javax.swing.JPanel();
        shiftHistogramButton = new javax.swing.JButton();
        scaleHistogramButton = new javax.swing.JButton();
        equalizeHistogramButton = new javax.swing.JButton();
        matchHistogramButton = new javax.swing.JButton();
        EqHistogramPanel = new javax.swing.JPanel();
        equalizeUniformButton = new javax.swing.JButton();
        equalizeExponentialButton = new javax.swing.JButton();
        equalizeRayleighButton = new javax.swing.JButton();
        equalizeHyperbolicRootsButton = new javax.swing.JButton();
        equalizeHyperbolicLogarithmicButton = new javax.swing.JButton();
        nonlinearFilterPanel = new javax.swing.JPanel();
        minFilterButton = new javax.swing.JButton();
        medianFilterButton1 = new javax.swing.JButton();
        maxFilterButton = new javax.swing.JButton();
        midpointFilterButton = new javax.swing.JButton();
        alphaTrimmedFilterButton = new javax.swing.JButton();
        harmonicMeanFilterButton = new javax.swing.JButton();
        contraHarmonicFilterButton = new javax.swing.JButton();
        geometricMeanFilterButton = new javax.swing.JButton();
        maxMinFilterButton = new javax.swing.JButton();
        arithmeticMeanFilterButton = new javax.swing.JButton();
        contraGeometricMeanFilterButton = new javax.swing.JButton();
        modeFilterButton = new javax.swing.JButton();
        compararFiltrosButton = new javax.swing.JButton();
        MorfologiaPanel = new javax.swing.JPanel();
        BinaryErotionButton = new javax.swing.JButton();
        BinaryDilationButton = new javax.swing.JButton();
        GrayScaleErotionButton = new javax.swing.JButton();
        GrayScaleDilationButton = new javax.swing.JButton();
        BinaryOpeningButton = new javax.swing.JButton();
        BinaryClosingButton = new javax.swing.JButton();
        GrayScaleClosingButton = new javax.swing.JButton();
        GrayScaleOpeningButton = new javax.swing.JButton();
        linearFilterPanel = new javax.swing.JPanel();
        homogeneityOperatorButton = new javax.swing.JButton();
        gradientFirstOrderButton = new javax.swing.JButton();
        differenceOperatorButton = new javax.swing.JButton();
        prewittButton = new javax.swing.JButton();
        sobelButton = new javax.swing.JButton();
        freiChenButton = new javax.swing.JButton();
        compassGradientButton = new javax.swing.JButton();
        laplacianButton = new javax.swing.JButton();
        prewittSecondOrderButton = new javax.swing.JButton();
        kirschButton = new javax.swing.JButton();
        notButton1 = new javax.swing.JButton();
        lessThanButton1 = new javax.swing.JButton();
        lessThanOrEqualButton1 = new javax.swing.JButton();
        greaterThanButton1 = new javax.swing.JButton();
        histogramPanel = new javax.swing.JPanel();
        showHistogramButton = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setBackground(new java.awt.Color(240, 240, 245));

        topPanel.setBackground(new java.awt.Color(230, 230, 235));

        loadButton.setBackground(new java.awt.Color(204, 204, 204));
        loadButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        loadButton.setText("Cargar");

        saveButton.setBackground(new java.awt.Color(204, 204, 204));
        saveButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        saveButton.setText("Guardar");

        resetButton.setBackground(new java.awt.Color(204, 204, 204));
        resetButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        resetButton.setText("Reset");

        javax.swing.GroupLayout topPanelLayout = new javax.swing.GroupLayout(topPanel);
        topPanel.setLayout(topPanelLayout);
        topPanelLayout.setHorizontalGroup(
            topPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(topPanelLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(loadButton)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(saveButton)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(resetButton, javax.swing.GroupLayout.PREFERRED_SIZE, 70, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        topPanelLayout.setVerticalGroup(
            topPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(topPanelLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(topPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addComponent(loadButton, javax.swing.GroupLayout.DEFAULT_SIZE, 37, Short.MAX_VALUE)
                    .addComponent(saveButton, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(resetButton, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        leftPanel.setBackground(new java.awt.Color(245, 245, 250));
        leftPanel.setBorder(javax.swing.BorderFactory.createTitledBorder(null, "Ajustes", javax.swing.border.TitledBorder.DEFAULT_JUSTIFICATION, javax.swing.border.TitledBorder.DEFAULT_POSITION, new java.awt.Font("Segoe UI", 0, 18))); // NOI18N
        leftPanel.setToolTipText("");
        leftPanel.setName(""); // NOI18N

        sliderPanel1.setBorder(javax.swing.BorderFactory.createTitledBorder(null, "Brillo", javax.swing.border.TitledBorder.DEFAULT_JUSTIFICATION, javax.swing.border.TitledBorder.DEFAULT_POSITION, new java.awt.Font("Segoe UI", 0, 14))); // NOI18N

        brightnessSlider.setMajorTickSpacing(50);
        brightnessSlider.setMinimum(-100);
        brightnessSlider.setMinorTickSpacing(10);
        brightnessSlider.setPaintLabels(true);
        brightnessSlider.setPaintTicks(true);
        brightnessSlider.setSnapToTicks(true);
        brightnessSlider.setValue(0);

        javax.swing.GroupLayout sliderPanel1Layout = new javax.swing.GroupLayout(sliderPanel1);
        sliderPanel1.setLayout(sliderPanel1Layout);
        sliderPanel1Layout.setHorizontalGroup(
            sliderPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(sliderPanel1Layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(brightnessSlider, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        sliderPanel1Layout.setVerticalGroup(
            sliderPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(sliderPanel1Layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(brightnessSlider, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        sliderPanel2.setBorder(javax.swing.BorderFactory.createTitledBorder(null, "Contraste", javax.swing.border.TitledBorder.DEFAULT_JUSTIFICATION, javax.swing.border.TitledBorder.DEFAULT_POSITION, new java.awt.Font("Segoe UI", 0, 14))); // NOI18N

        contrastSlider.setMajorTickSpacing(50);
        contrastSlider.setMaximum(200);
        contrastSlider.setMinimum(50);
        contrastSlider.setMinorTickSpacing(10);
        contrastSlider.setPaintLabels(true);
        contrastSlider.setPaintTicks(true);
        contrastSlider.setSnapToTicks(true);
        contrastSlider.setValue(100);

        javax.swing.GroupLayout sliderPanel2Layout = new javax.swing.GroupLayout(sliderPanel2);
        sliderPanel2.setLayout(sliderPanel2Layout);
        sliderPanel2Layout.setHorizontalGroup(
            sliderPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(sliderPanel2Layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(contrastSlider, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        sliderPanel2Layout.setVerticalGroup(
            sliderPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(sliderPanel2Layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(contrastSlider, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        javax.swing.GroupLayout leftPanelLayout = new javax.swing.GroupLayout(leftPanel);
        leftPanel.setLayout(leftPanelLayout);
        leftPanelLayout.setHorizontalGroup(
            leftPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(leftPanelLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(leftPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(sliderPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(sliderPanel2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addContainerGap())
        );
        leftPanelLayout.setVerticalGroup(
            leftPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, leftPanelLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(sliderPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGap(12, 12, 12)
                .addComponent(sliderPanel2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addContainerGap())
        );

        imageScrollPane.setBorder(javax.swing.BorderFactory.createTitledBorder(null, "Imagen", javax.swing.border.TitledBorder.DEFAULT_JUSTIFICATION, javax.swing.border.TitledBorder.DEFAULT_POSITION, new java.awt.Font("Segoe UI", 0, 18))); // NOI18N

        imageLabel.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        imageScrollPane.setViewportView(imageLabel);

        grayButton.setBackground(new java.awt.Color(204, 204, 204));
        grayButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        grayButton.setText("Escala de Grises");

        redButton.setBackground(new java.awt.Color(204, 204, 204));
        redButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        redButton.setText("Rojo");

        greenButton.setBackground(new java.awt.Color(204, 204, 204));
        greenButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        greenButton.setText("Verde");

        blueButton.setBackground(new java.awt.Color(204, 204, 204));
        blueButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        blueButton.setText("Azul");

        yiqButton1.setBackground(new java.awt.Color(204, 204, 204));
        yiqButton1.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        yiqButton1.setText("Convertir a YIQ (Y)");

        hsvButton1.setBackground(new java.awt.Color(204, 204, 204));
        hsvButton1.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        hsvButton1.setText("Convertir a HSV (V)");

        hsiButton1.setBackground(new java.awt.Color(204, 204, 204));
        hsiButton1.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        hsiButton1.setText("Convertir a HSI (I)");

        cannyEdgeButton.setBackground(new java.awt.Color(204, 204, 204));
        cannyEdgeButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        cannyEdgeButton.setText("Detección Canny");

        javax.swing.GroupLayout filterPanelLayout = new javax.swing.GroupLayout(filterPanel);
        filterPanel.setLayout(filterPanelLayout);
        filterPanelLayout.setHorizontalGroup(
            filterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(filterPanelLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(filterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(filterPanelLayout.createSequentialGroup()
                        .addComponent(grayButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 29, Short.MAX_VALUE)
                        .addComponent(redButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(filterPanelLayout.createSequentialGroup()
                        .addComponent(greenButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(blueButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(filterPanelLayout.createSequentialGroup()
                        .addComponent(yiqButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(hsvButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(filterPanelLayout.createSequentialGroup()
                        .addComponent(hsiButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(cannyEdgeButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap())
        );
        filterPanelLayout.setVerticalGroup(
            filterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(filterPanelLayout.createSequentialGroup()
                .addContainerGap(56, Short.MAX_VALUE)
                .addGroup(filterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(grayButton, javax.swing.GroupLayout.PREFERRED_SIZE, 125, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(redButton, javax.swing.GroupLayout.PREFERRED_SIZE, 125, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(filterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(greenButton, javax.swing.GroupLayout.PREFERRED_SIZE, 125, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(blueButton, javax.swing.GroupLayout.PREFERRED_SIZE, 125, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(filterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(yiqButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 125, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(hsvButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 125, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(filterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(hsiButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 125, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(cannyEdgeButton, javax.swing.GroupLayout.PREFERRED_SIZE, 125, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(55, Short.MAX_VALUE))
        );

        rightPanel.addTab("Filtros", filterPanel);

        gaussianNoiseButton.setBackground(new java.awt.Color(204, 204, 204));
        gaussianNoiseButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        gaussianNoiseButton.setText("Ruido Gaussiano");

        saltPepperNoiseButton.setBackground(new java.awt.Color(204, 204, 204));
        saltPepperNoiseButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        saltPepperNoiseButton.setText("Ruido Sal y Pimienta");

        uniformNoiseButton.setBackground(new java.awt.Color(204, 204, 204));
        uniformNoiseButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        uniformNoiseButton.setText("Ruido Uniforme");

        rayleighNoiseButton.setBackground(new java.awt.Color(204, 204, 204));
        rayleighNoiseButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        rayleighNoiseButton.setText("Ruido Rayleigh");

        exponentialNoiseButton.setBackground(new java.awt.Color(204, 204, 204));
        exponentialNoiseButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        exponentialNoiseButton.setText("Ruido Exponencial");

        gammaNoiseButton.setBackground(new java.awt.Color(204, 204, 204));
        gammaNoiseButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        gammaNoiseButton.setText("Ruido Gamma");

        coherentNoiseButton.setBackground(new java.awt.Color(204, 204, 204));
        coherentNoiseButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        coherentNoiseButton.setText("Ruido Coherente");

        saltNoiseButton.setBackground(new java.awt.Color(204, 204, 204));
        saltNoiseButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        saltNoiseButton.setText("Ruido Sal");

        pepperNoiseButton.setBackground(new java.awt.Color(204, 204, 204));
        pepperNoiseButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        pepperNoiseButton.setText("Ruido Pimienta");

        javax.swing.GroupLayout noisePanelLayout = new javax.swing.GroupLayout(noisePanel);
        noisePanel.setLayout(noisePanelLayout);
        noisePanelLayout.setHorizontalGroup(
            noisePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(noisePanelLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(noisePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(noisePanelLayout.createSequentialGroup()
                        .addComponent(uniformNoiseButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 35, Short.MAX_VALUE)
                        .addComponent(rayleighNoiseButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(noisePanelLayout.createSequentialGroup()
                        .addComponent(exponentialNoiseButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(gammaNoiseButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(noisePanelLayout.createSequentialGroup()
                        .addGroup(noisePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(gaussianNoiseButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(coherentNoiseButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addGroup(noisePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(saltPepperNoiseButton, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(saltNoiseButton, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGroup(noisePanelLayout.createSequentialGroup()
                        .addComponent(pepperNoiseButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(0, 0, Short.MAX_VALUE)))
                .addContainerGap())
        );
        noisePanelLayout.setVerticalGroup(
            noisePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(noisePanelLayout.createSequentialGroup()
                .addGap(27, 27, 27)
                .addGroup(noisePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addComponent(gaussianNoiseButton, javax.swing.GroupLayout.DEFAULT_SIZE, 112, Short.MAX_VALUE)
                    .addComponent(saltPepperNoiseButton, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addGap(18, 18, 18)
                .addGroup(noisePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(uniformNoiseButton, javax.swing.GroupLayout.PREFERRED_SIZE, 112, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(rayleighNoiseButton, javax.swing.GroupLayout.PREFERRED_SIZE, 112, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(noisePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(exponentialNoiseButton, javax.swing.GroupLayout.PREFERRED_SIZE, 112, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(gammaNoiseButton, javax.swing.GroupLayout.PREFERRED_SIZE, 112, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(noisePanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(coherentNoiseButton, javax.swing.GroupLayout.PREFERRED_SIZE, 112, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(saltNoiseButton, javax.swing.GroupLayout.PREFERRED_SIZE, 112, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addComponent(pepperNoiseButton, javax.swing.GroupLayout.PREFERRED_SIZE, 112, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        rightPanel.addTab("Ruidos", noisePanel);

        rgbToCMYButton.setBackground(new java.awt.Color(204, 204, 204));
        rgbToCMYButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        rgbToCMYButton.setText("RGB → CMY");

        cmyToRGBButton.setBackground(new java.awt.Color(204, 204, 204));
        cmyToRGBButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        cmyToRGBButton.setText("CMY → RGB");

        rgbToYIQButton.setBackground(new java.awt.Color(204, 204, 204));
        rgbToYIQButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        rgbToYIQButton.setText("RGB → YIQ");

        yiqToRGBButton.setBackground(new java.awt.Color(204, 204, 204));
        yiqToRGBButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        yiqToRGBButton.setText("YIQ → RGB");

        rgbToHSIButton.setBackground(new java.awt.Color(204, 204, 204));
        rgbToHSIButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        rgbToHSIButton.setText("RGB → HSI");

        hsiToRGBButton.setBackground(new java.awt.Color(204, 204, 204));
        hsiToRGBButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        hsiToRGBButton.setText("HSI → RGB");

        cmyToCMYKButton.setBackground(new java.awt.Color(204, 204, 204));
        cmyToCMYKButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        cmyToCMYKButton.setText("CMY → CMYK");

        rgbToHSVButton.setBackground(new java.awt.Color(204, 204, 204));
        rgbToHSVButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        rgbToHSVButton.setText("RGB → HSV");

        hsvToRGBButton.setBackground(new java.awt.Color(204, 204, 204));
        hsvToRGBButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        hsvToRGBButton.setText("HSV → RGB");

        rgbToLabButton.setBackground(new java.awt.Color(204, 204, 204));
        rgbToLabButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        rgbToLabButton.setText("RGB → Lab");

        labToRGBButton.setBackground(new java.awt.Color(204, 204, 204));
        labToRGBButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        labToRGBButton.setText("Lab → RGB");

        javax.swing.GroupLayout conversionPanelLayout = new javax.swing.GroupLayout(conversionPanel);
        conversionPanel.setLayout(conversionPanelLayout);
        conversionPanelLayout.setHorizontalGroup(
            conversionPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(conversionPanelLayout.createSequentialGroup()
                .addContainerGap(12, Short.MAX_VALUE)
                .addGroup(conversionPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(labToRGBButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(conversionPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                        .addGroup(conversionPanelLayout.createSequentialGroup()
                            .addComponent(hsvToRGBButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                            .addComponent(rgbToLabButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGroup(conversionPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(conversionPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                .addGroup(conversionPanelLayout.createSequentialGroup()
                                    .addComponent(cmyToCMYKButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                    .addComponent(rgbToHSVButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addGroup(conversionPanelLayout.createSequentialGroup()
                                    .addComponent(rgbToHSIButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                    .addComponent(hsiToRGBButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)))
                            .addGroup(conversionPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                .addGroup(conversionPanelLayout.createSequentialGroup()
                                    .addComponent(rgbToYIQButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                    .addComponent(yiqToRGBButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addGroup(conversionPanelLayout.createSequentialGroup()
                                    .addComponent(rgbToCMYButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                    .addComponent(cmyToRGBButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))))))
                .addContainerGap(13, Short.MAX_VALUE))
        );
        conversionPanelLayout.setVerticalGroup(
            conversionPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(conversionPanelLayout.createSequentialGroup()
                .addContainerGap(78, Short.MAX_VALUE)
                .addGroup(conversionPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(rgbToCMYButton, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(cmyToRGBButton, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(conversionPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(rgbToYIQButton, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(yiqToRGBButton, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(conversionPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(rgbToHSIButton, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(hsiToRGBButton, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(conversionPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(cmyToCMYKButton, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(rgbToHSVButton, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(conversionPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(hsvToRGBButton, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(rgbToLabButton, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(labToRGBButton, javax.swing.GroupLayout.PREFERRED_SIZE, 75, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(77, Short.MAX_VALUE))
        );

        rightPanel.addTab("Conversiones", conversionPanel);

        binarization1Button.setBackground(new java.awt.Color(204, 204, 204));
        binarization1Button.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        binarization1Button.setText("1 umbral (Y)");

        binarization2Button.setBackground(new java.awt.Color(204, 204, 204));
        binarization2Button.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        binarization2Button.setText("2 umbrales (Y)");

        binarization3Button.setBackground(new java.awt.Color(204, 204, 204));
        binarization3Button.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        binarization3Button.setText("3 umbrales (Y)");

        invertBinButton.setBackground(new java.awt.Color(204, 204, 204));
        invertBinButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        invertBinButton.setText("Invertir Binarización");

        binarizationToRGBButton.setBackground(new java.awt.Color(204, 204, 204));
        binarizationToRGBButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        binarizationToRGBButton.setText("Bin → RGB");

        javax.swing.GroupLayout binarizationPanelLayout = new javax.swing.GroupLayout(binarizationPanel);
        binarizationPanel.setLayout(binarizationPanelLayout);
        binarizationPanelLayout.setHorizontalGroup(
            binarizationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(binarizationPanelLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(binarizationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, binarizationPanelLayout.createSequentialGroup()
                        .addComponent(binarization1Button, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 29, Short.MAX_VALUE)
                        .addComponent(binarization2Button, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, binarizationPanelLayout.createSequentialGroup()
                        .addComponent(binarization3Button, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(invertBinButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(binarizationPanelLayout.createSequentialGroup()
                        .addComponent(binarizationToRGBButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(0, 0, Short.MAX_VALUE)))
                .addContainerGap())
        );
        binarizationPanelLayout.setVerticalGroup(
            binarizationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(binarizationPanelLayout.createSequentialGroup()
                .addContainerGap(97, Short.MAX_VALUE)
                .addGroup(binarizationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(binarization1Button, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(binarization2Button, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(binarizationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(binarization3Button, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(invertBinButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addComponent(binarizationToRGBButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(97, Short.MAX_VALUE))
        );

        rightPanel.addTab("Binarización", binarizationPanel);

        translationButton.setBackground(new java.awt.Color(204, 204, 204));
        translationButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        translationButton.setText("Traslacion");

        rotationButton.setBackground(new java.awt.Color(204, 204, 204));
        rotationButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        rotationButton.setText("Rotacion");

        interpolationButton.setBackground(new java.awt.Color(204, 204, 204));
        interpolationButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        interpolationButton.setText("Interpolacion");

        sumButton.setBackground(new java.awt.Color(204, 204, 204));
        sumButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        sumButton.setText("Suma");

        subtractionButton.setBackground(new java.awt.Color(204, 204, 204));
        subtractionButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        subtractionButton.setText("Resta");

        multiplicationButton.setBackground(new java.awt.Color(204, 204, 204));
        multiplicationButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        multiplicationButton.setText("Multiplicacion");

        divisionButton.setBackground(new java.awt.Color(204, 204, 204));
        divisionButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        divisionButton.setText("Division");

        andButton.setBackground(new java.awt.Color(204, 204, 204));
        andButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        andButton.setText("And");

        orButton.setBackground(new java.awt.Color(204, 204, 204));
        orButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        orButton.setText("Or");

        xorButton.setBackground(new java.awt.Color(204, 204, 204));
        xorButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        xorButton.setText("Xor");

        notButton.setBackground(new java.awt.Color(204, 204, 204));
        notButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        notButton.setText("Not");

        lessThanButton.setBackground(new java.awt.Color(204, 204, 204));
        lessThanButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        lessThanButton.setText("<");

        lessThanOrEqualButton.setBackground(new java.awt.Color(204, 204, 204));
        lessThanOrEqualButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        lessThanOrEqualButton.setText("<=");

        greaterThanButton.setBackground(new java.awt.Color(204, 204, 204));
        greaterThanButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        greaterThanButton.setText(">");

        greaterThanOrEqualButton.setBackground(new java.awt.Color(204, 204, 204));
        greaterThanOrEqualButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        greaterThanOrEqualButton.setText(">=");

        equalButton.setBackground(new java.awt.Color(204, 204, 204));
        equalButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        equalButton.setText("==");

        notEqualButton.setBackground(new java.awt.Color(204, 204, 204));
        notEqualButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        notEqualButton.setText("!=");

        javax.swing.GroupLayout operationPanelLayout = new javax.swing.GroupLayout(operationPanel);
        operationPanel.setLayout(operationPanelLayout);
        operationPanelLayout.setHorizontalGroup(
            operationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(operationPanelLayout.createSequentialGroup()
                .addContainerGap(12, Short.MAX_VALUE)
                .addGroup(operationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(operationPanelLayout.createSequentialGroup()
                        .addComponent(translationButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(rotationButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(operationPanelLayout.createSequentialGroup()
                        .addComponent(interpolationButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(sumButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(operationPanelLayout.createSequentialGroup()
                        .addComponent(subtractionButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(multiplicationButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(operationPanelLayout.createSequentialGroup()
                        .addComponent(divisionButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(andButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(operationPanelLayout.createSequentialGroup()
                        .addComponent(orButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(xorButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(operationPanelLayout.createSequentialGroup()
                        .addComponent(notButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(lessThanButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(operationPanelLayout.createSequentialGroup()
                        .addComponent(lessThanOrEqualButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(greaterThanButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(operationPanelLayout.createSequentialGroup()
                        .addComponent(greaterThanOrEqualButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(equalButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addComponent(notEqualButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(13, Short.MAX_VALUE))
        );
        operationPanelLayout.setVerticalGroup(
            operationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(operationPanelLayout.createSequentialGroup()
                .addContainerGap(39, Short.MAX_VALUE)
                .addGroup(operationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(translationButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(rotationButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(operationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(interpolationButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(sumButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(operationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(subtractionButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(multiplicationButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(operationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(divisionButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(andButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(operationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(orButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(xorButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(operationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(notButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(lessThanButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(operationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lessThanOrEqualButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(greaterThanButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(operationPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(greaterThanOrEqualButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(equalButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(notEqualButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(38, Short.MAX_VALUE))
        );

        rightPanel.addTab("Operaciones", operationPanel);

        shiftHistogramButton.setBackground(new java.awt.Color(204, 204, 204));
        shiftHistogramButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        shiftHistogramButton.setText("Desplazamiento");

        scaleHistogramButton.setBackground(new java.awt.Color(204, 204, 204));
        scaleHistogramButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        scaleHistogramButton.setText("Contracción/Expansion");

        equalizeHistogramButton.setBackground(new java.awt.Color(204, 204, 204));
        equalizeHistogramButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        equalizeHistogramButton.setText("Ecualización");

        matchHistogramButton.setBackground(new java.awt.Color(204, 204, 204));
        matchHistogramButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        matchHistogramButton.setText("Igualación");

        javax.swing.GroupLayout modHistogramPanelLayout = new javax.swing.GroupLayout(modHistogramPanel);
        modHistogramPanel.setLayout(modHistogramPanelLayout);
        modHistogramPanelLayout.setHorizontalGroup(
            modHistogramPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(modHistogramPanelLayout.createSequentialGroup()
                .addContainerGap(81, Short.MAX_VALUE)
                .addGroup(modHistogramPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addComponent(shiftHistogramButton, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(scaleHistogramButton, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(equalizeHistogramButton, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(matchHistogramButton, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addContainerGap(81, Short.MAX_VALUE))
        );
        modHistogramPanelLayout.setVerticalGroup(
            modHistogramPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(modHistogramPanelLayout.createSequentialGroup()
                .addContainerGap(57, Short.MAX_VALUE)
                .addComponent(shiftHistogramButton, javax.swing.GroupLayout.PREFERRED_SIZE, 110, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(37, 37, 37)
                .addComponent(scaleHistogramButton, javax.swing.GroupLayout.PREFERRED_SIZE, 110, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(37, 37, 37)
                .addComponent(equalizeHistogramButton, javax.swing.GroupLayout.PREFERRED_SIZE, 110, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(37, 37, 37)
                .addComponent(matchHistogramButton, javax.swing.GroupLayout.PREFERRED_SIZE, 110, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(57, Short.MAX_VALUE))
        );

        rightPanel.addTab("Mod. Histogramas", modHistogramPanel);

        equalizeUniformButton.setBackground(new java.awt.Color(204, 204, 204));
        equalizeUniformButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        equalizeUniformButton.setText("Uniforme");

        equalizeExponentialButton.setBackground(new java.awt.Color(204, 204, 204));
        equalizeExponentialButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        equalizeExponentialButton.setText("Exponencial");

        equalizeRayleighButton.setBackground(new java.awt.Color(204, 204, 204));
        equalizeRayleighButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        equalizeRayleighButton.setText("Rayleigh");

        equalizeHyperbolicRootsButton.setBackground(new java.awt.Color(204, 204, 204));
        equalizeHyperbolicRootsButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        equalizeHyperbolicRootsButton.setText("Raíces");

        equalizeHyperbolicLogarithmicButton.setBackground(new java.awt.Color(204, 204, 204));
        equalizeHyperbolicLogarithmicButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        equalizeHyperbolicLogarithmicButton.setText("Logaritmicas");

        javax.swing.GroupLayout EqHistogramPanelLayout = new javax.swing.GroupLayout(EqHistogramPanel);
        EqHistogramPanel.setLayout(EqHistogramPanelLayout);
        EqHistogramPanelLayout.setHorizontalGroup(
            EqHistogramPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(EqHistogramPanelLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(EqHistogramPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, EqHistogramPanelLayout.createSequentialGroup()
                        .addComponent(equalizeUniformButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 29, Short.MAX_VALUE)
                        .addComponent(equalizeExponentialButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, EqHistogramPanelLayout.createSequentialGroup()
                        .addComponent(equalizeRayleighButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(equalizeHyperbolicRootsButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(EqHistogramPanelLayout.createSequentialGroup()
                        .addComponent(equalizeHyperbolicLogarithmicButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(0, 0, Short.MAX_VALUE)))
                .addContainerGap())
        );
        EqHistogramPanelLayout.setVerticalGroup(
            EqHistogramPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(EqHistogramPanelLayout.createSequentialGroup()
                .addContainerGap(97, Short.MAX_VALUE)
                .addGroup(EqHistogramPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(equalizeUniformButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(equalizeExponentialButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(EqHistogramPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(equalizeRayleighButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(equalizeHyperbolicRootsButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addComponent(equalizeHyperbolicLogarithmicButton, javax.swing.GroupLayout.PREFERRED_SIZE, 145, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(97, Short.MAX_VALUE))
        );

        rightPanel.addTab("EQ Histogramas", EqHistogramPanel);

        minFilterButton.setBackground(new java.awt.Color(204, 204, 204));
        minFilterButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        minFilterButton.setText("Filtro del Mínimo");

        medianFilterButton1.setBackground(new java.awt.Color(204, 204, 204));
        medianFilterButton1.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        medianFilterButton1.setText("Filtro de Mediana");

        maxFilterButton.setBackground(new java.awt.Color(204, 204, 204));
        maxFilterButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        maxFilterButton.setText("Filtro del Máximo");

        midpointFilterButton.setBackground(new java.awt.Color(204, 204, 204));
        midpointFilterButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        midpointFilterButton.setText("Filtro Punto Medio");

        alphaTrimmedFilterButton.setBackground(new java.awt.Color(204, 204, 204));
        alphaTrimmedFilterButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        alphaTrimmedFilterButton.setText("Filtro Alfa Recortado");

        harmonicMeanFilterButton.setBackground(new java.awt.Color(204, 204, 204));
        harmonicMeanFilterButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        harmonicMeanFilterButton.setText("Filtro Armónico Inferior");

        contraHarmonicFilterButton.setBackground(new java.awt.Color(204, 204, 204));
        contraHarmonicFilterButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        contraHarmonicFilterButton.setText("Filtro Contra-Armónico");

        geometricMeanFilterButton.setBackground(new java.awt.Color(204, 204, 204));
        geometricMeanFilterButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        geometricMeanFilterButton.setText("Filtro Geométrico Inferior");

        maxMinFilterButton.setBackground(new java.awt.Color(204, 204, 204));
        maxMinFilterButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        maxMinFilterButton.setText("Filtro Máximo - Mínimo");

        arithmeticMeanFilterButton.setBackground(new java.awt.Color(204, 204, 204));
        arithmeticMeanFilterButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        arithmeticMeanFilterButton.setText("Filtro Media Aritmética");

        contraGeometricMeanFilterButton.setBackground(new java.awt.Color(204, 204, 204));
        contraGeometricMeanFilterButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        contraGeometricMeanFilterButton.setText("Filtro Contra-Geométrico");

        modeFilterButton.setBackground(new java.awt.Color(204, 204, 204));
        modeFilterButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        modeFilterButton.setText("Filtro de Moda");

        compararFiltrosButton.setBackground(new java.awt.Color(204, 204, 204));
        compararFiltrosButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        compararFiltrosButton.setText("Comparación de resultados");

        javax.swing.GroupLayout nonlinearFilterPanelLayout = new javax.swing.GroupLayout(nonlinearFilterPanel);
        nonlinearFilterPanel.setLayout(nonlinearFilterPanelLayout);
        nonlinearFilterPanelLayout.setHorizontalGroup(
            nonlinearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(nonlinearFilterPanelLayout.createSequentialGroup()
                .addContainerGap(16, Short.MAX_VALUE)
                .addGroup(nonlinearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(compararFiltrosButton, javax.swing.GroupLayout.PREFERRED_SIZE, 140, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(contraGeometricMeanFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 140, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(maxMinFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 140, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(contraHarmonicFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 140, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(alphaTrimmedFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 140, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(maxFilterButton)
                    .addComponent(medianFilterButton1))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 25, Short.MAX_VALUE)
                .addGroup(nonlinearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, nonlinearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                        .addComponent(minFilterButton, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(midpointFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 1, Short.MAX_VALUE)
                        .addComponent(harmonicMeanFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 1, Short.MAX_VALUE)
                        .addComponent(geometricMeanFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 1, Short.MAX_VALUE))
                    .addComponent(arithmeticMeanFilterButton, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 140, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(modeFilterButton, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 140, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(16, Short.MAX_VALUE))
        );
        nonlinearFilterPanelLayout.setVerticalGroup(
            nonlinearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(nonlinearFilterPanelLayout.createSequentialGroup()
                .addGap(17, 17, 17)
                .addGroup(nonlinearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(minFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(medianFilterButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(nonlinearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(maxFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(midpointFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(nonlinearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(alphaTrimmedFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(harmonicMeanFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(nonlinearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(contraHarmonicFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(geometricMeanFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(nonlinearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(maxMinFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(arithmeticMeanFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(nonlinearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(contraGeometricMeanFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(modeFilterButton, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addComponent(compararFiltrosButton, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(274, Short.MAX_VALUE))
        );

        rightPanel.addTab("Filtros no lineales", nonlinearFilterPanel);

        BinaryErotionButton.setBackground(new java.awt.Color(204, 204, 204));
        BinaryErotionButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        BinaryErotionButton.setText("Erosión Binaria");

        BinaryDilationButton.setBackground(new java.awt.Color(204, 204, 204));
        BinaryDilationButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        BinaryDilationButton.setText("Dilatación Binaria");

        GrayScaleErotionButton.setBackground(new java.awt.Color(204, 204, 204));
        GrayScaleErotionButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        GrayScaleErotionButton.setText("Erosión Escala de Grises");

        GrayScaleDilationButton.setBackground(new java.awt.Color(204, 204, 204));
        GrayScaleDilationButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        GrayScaleDilationButton.setText("Dilatación Escala de Grises");

        BinaryOpeningButton.setBackground(new java.awt.Color(204, 204, 204));
        BinaryOpeningButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        BinaryOpeningButton.setText("Apertura Binaria");

        BinaryClosingButton.setBackground(new java.awt.Color(204, 204, 204));
        BinaryClosingButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        BinaryClosingButton.setText("Cierre Binaria");
        BinaryClosingButton.setToolTipText("");

        GrayScaleClosingButton.setBackground(new java.awt.Color(204, 204, 204));
        GrayScaleClosingButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        GrayScaleClosingButton.setText("Cierre Escala Grises");

        GrayScaleOpeningButton.setBackground(new java.awt.Color(204, 204, 204));
        GrayScaleOpeningButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        GrayScaleOpeningButton.setText("Apertura Escala Grises");

        javax.swing.GroupLayout MorfologiaPanelLayout = new javax.swing.GroupLayout(MorfologiaPanel);
        MorfologiaPanel.setLayout(MorfologiaPanelLayout);
        MorfologiaPanelLayout.setHorizontalGroup(
            MorfologiaPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(MorfologiaPanelLayout.createSequentialGroup()
                .addGap(21, 21, 21)
                .addGroup(MorfologiaPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(MorfologiaPanelLayout.createSequentialGroup()
                        .addComponent(GrayScaleOpeningButton, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addComponent(GrayScaleClosingButton, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(MorfologiaPanelLayout.createSequentialGroup()
                        .addComponent(BinaryErotionButton, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addComponent(BinaryDilationButton))
                    .addGroup(MorfologiaPanelLayout.createSequentialGroup()
                        .addGroup(MorfologiaPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                            .addComponent(GrayScaleErotionButton, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.PREFERRED_SIZE, 0, Short.MAX_VALUE)
                            .addComponent(BinaryOpeningButton, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 135, Short.MAX_VALUE))
                        .addGap(18, 18, 18)
                        .addGroup(MorfologiaPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(BinaryClosingButton, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(GrayScaleDilationButton, javax.swing.GroupLayout.PREFERRED_SIZE, 0, Short.MAX_VALUE))))
                .addContainerGap(28, Short.MAX_VALUE))
        );
        MorfologiaPanelLayout.setVerticalGroup(
            MorfologiaPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(MorfologiaPanelLayout.createSequentialGroup()
                .addGap(31, 31, 31)
                .addGroup(MorfologiaPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(BinaryErotionButton)
                    .addComponent(BinaryDilationButton))
                .addGap(18, 18, 18)
                .addGroup(MorfologiaPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(BinaryOpeningButton)
                    .addComponent(BinaryClosingButton))
                .addGap(18, 18, 18)
                .addGroup(MorfologiaPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addComponent(GrayScaleErotionButton, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(GrayScaleDilationButton, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addGap(18, 18, 18)
                .addGroup(MorfologiaPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(GrayScaleOpeningButton)
                    .addComponent(GrayScaleClosingButton))
                .addContainerGap(472, Short.MAX_VALUE))
        );

        rightPanel.addTab("Morfologias", MorfologiaPanel);

        homogeneityOperatorButton.setBackground(new java.awt.Color(204, 204, 204));
        homogeneityOperatorButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        homogeneityOperatorButton.setText("Operador de Homogeneidad");

        gradientFirstOrderButton.setBackground(new java.awt.Color(204, 204, 204));
        gradientFirstOrderButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        gradientFirstOrderButton.setText("Gradiente Primer Orden");

        differenceOperatorButton.setBackground(new java.awt.Color(204, 204, 204));
        differenceOperatorButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        differenceOperatorButton.setText("Operador de Diferencia");

        prewittButton.setBackground(new java.awt.Color(204, 204, 204));
        prewittButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        prewittButton.setText("Filtro Prewitt");

        sobelButton.setBackground(new java.awt.Color(204, 204, 204));
        sobelButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        sobelButton.setText("Filtro Sobel");

        freiChenButton.setBackground(new java.awt.Color(204, 204, 204));
        freiChenButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        freiChenButton.setText("Filtro Frei-Chen");

        compassGradientButton.setBackground(new java.awt.Color(204, 204, 204));
        compassGradientButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        compassGradientButton.setText("Gradiente Compás");

        laplacianButton.setBackground(new java.awt.Color(204, 204, 204));
        laplacianButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        laplacianButton.setText("Filtro Laplaciano");

        prewittSecondOrderButton.setBackground(new java.awt.Color(204, 204, 204));
        prewittSecondOrderButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        prewittSecondOrderButton.setText("Prewitt 2° Orden");
        prewittSecondOrderButton.setToolTipText("");

        kirschButton.setBackground(new java.awt.Color(204, 204, 204));
        kirschButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        kirschButton.setText("Filtro Kirsch");

        notButton1.setBackground(new java.awt.Color(204, 204, 204));
        notButton1.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        notButton1.setText("Filtro Robinson");

        lessThanButton1.setBackground(new java.awt.Color(204, 204, 204));
        lessThanButton1.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        lessThanButton1.setText("<");

        lessThanOrEqualButton1.setBackground(new java.awt.Color(204, 204, 204));
        lessThanOrEqualButton1.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        lessThanOrEqualButton1.setText("<=");

        greaterThanButton1.setBackground(new java.awt.Color(204, 204, 204));
        greaterThanButton1.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        greaterThanButton1.setText(">");

        javax.swing.GroupLayout linearFilterPanelLayout = new javax.swing.GroupLayout(linearFilterPanel);
        linearFilterPanel.setLayout(linearFilterPanelLayout);
        linearFilterPanelLayout.setHorizontalGroup(
            linearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 337, Short.MAX_VALUE)
            .addGroup(linearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(linearFilterPanelLayout.createSequentialGroup()
                    .addGap(15, 15, 15)
                    .addGroup(linearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addGroup(linearFilterPanelLayout.createSequentialGroup()
                            .addComponent(homogeneityOperatorButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                            .addComponent(gradientFirstOrderButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGroup(linearFilterPanelLayout.createSequentialGroup()
                            .addComponent(differenceOperatorButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                            .addComponent(prewittButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGroup(linearFilterPanelLayout.createSequentialGroup()
                            .addComponent(sobelButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                            .addComponent(freiChenButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGroup(linearFilterPanelLayout.createSequentialGroup()
                            .addComponent(compassGradientButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                            .addComponent(laplacianButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGroup(linearFilterPanelLayout.createSequentialGroup()
                            .addComponent(prewittSecondOrderButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                            .addComponent(kirschButton, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGroup(linearFilterPanelLayout.createSequentialGroup()
                            .addComponent(notButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                            .addComponent(lessThanButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGroup(linearFilterPanelLayout.createSequentialGroup()
                            .addComponent(lessThanOrEqualButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                            .addComponent(greaterThanButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 150, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addContainerGap(16, Short.MAX_VALUE)))
        );
        linearFilterPanelLayout.setVerticalGroup(
            linearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 665, Short.MAX_VALUE)
            .addGroup(linearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                .addGroup(linearFilterPanelLayout.createSequentialGroup()
                    .addGap(115, 115, 115)
                    .addGroup(linearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(homogeneityOperatorButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(gradientFirstOrderButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                    .addGroup(linearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(differenceOperatorButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(prewittButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                    .addGroup(linearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(sobelButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(freiChenButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                    .addGroup(linearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(compassGradientButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(laplacianButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                    .addGroup(linearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(prewittSecondOrderButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(kirschButton, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                    .addGroup(linearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(notButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(lessThanButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                    .addGroup(linearFilterPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(lessThanOrEqualButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(greaterThanButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addContainerGap(94, Short.MAX_VALUE)))
        );

        rightPanel.addTab("Filtros Lineales", linearFilterPanel);

        histogramPanel.setBackground(new java.awt.Color(245, 245, 250));
        histogramPanel.setBorder(javax.swing.BorderFactory.createTitledBorder(null, "Histograma General", javax.swing.border.TitledBorder.DEFAULT_JUSTIFICATION, javax.swing.border.TitledBorder.DEFAULT_POSITION, new java.awt.Font("Segoe UI", 0, 18))); // NOI18N
        histogramPanel.setName(""); // NOI18N

        showHistogramButton.setBackground(new java.awt.Color(204, 204, 204));
        showHistogramButton.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        showHistogramButton.setText("Mostrar Histograma");

        javax.swing.GroupLayout histogramPanelLayout = new javax.swing.GroupLayout(histogramPanel);
        histogramPanel.setLayout(histogramPanelLayout);
        histogramPanelLayout.setHorizontalGroup(
            histogramPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, histogramPanelLayout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(showHistogramButton, javax.swing.GroupLayout.PREFERRED_SIZE, 200, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        histogramPanelLayout.setVerticalGroup(
            histogramPanelLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, histogramPanelLayout.createSequentialGroup()
                .addContainerGap(8, Short.MAX_VALUE)
                .addComponent(showHistogramButton, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(7, Short.MAX_VALUE))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(topPanel, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(leftPanel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addComponent(imageScrollPane, javax.swing.GroupLayout.DEFAULT_SIZE, 877, Short.MAX_VALUE)
                        .addGap(18, 18, 18)
                        .addComponent(rightPanel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addComponent(histogramPanel, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addComponent(topPanel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(12, 12, 12)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(leftPanel, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(rightPanel)
                    .addComponent(imageScrollPane))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(histogramPanel, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(12, 12, 12))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(ImagenVista.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(ImagenVista.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(ImagenVista.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(ImagenVista.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        
        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton BinaryClosingButton;
    private javax.swing.JButton BinaryDilationButton;
    private javax.swing.JButton BinaryErotionButton;
    private javax.swing.JButton BinaryOpeningButton;
    private javax.swing.JPanel EqHistogramPanel;
    private javax.swing.JButton GrayScaleClosingButton;
    private javax.swing.JButton GrayScaleDilationButton;
    private javax.swing.JButton GrayScaleErotionButton;
    private javax.swing.JButton GrayScaleOpeningButton;
    private javax.swing.JPanel MorfologiaPanel;
    private javax.swing.JButton alphaTrimmedFilterButton;
    private javax.swing.JButton andButton;
    private javax.swing.JButton arithmeticMeanFilterButton;
    private javax.swing.JButton binarization1Button;
    private javax.swing.JButton binarization2Button;
    private javax.swing.JButton binarization3Button;
    private javax.swing.JPanel binarizationPanel;
    private javax.swing.JButton binarizationToRGBButton;
    private javax.swing.JButton blueButton;
    private javax.swing.JSlider brightnessSlider;
    private javax.swing.JButton cannyEdgeButton;
    private javax.swing.JButton cmyToCMYKButton;
    private javax.swing.JButton cmyToRGBButton;
    private javax.swing.JButton coherentNoiseButton;
    private javax.swing.JButton compararFiltrosButton;
    private javax.swing.JButton compassGradientButton;
    private javax.swing.JButton contraGeometricMeanFilterButton;
    private javax.swing.JButton contraHarmonicFilterButton;
    private javax.swing.JSlider contrastSlider;
    private javax.swing.JPanel conversionPanel;
    private javax.swing.JButton differenceOperatorButton;
    private javax.swing.JButton divisionButton;
    private javax.swing.JButton equalButton;
    private javax.swing.JButton equalizeExponentialButton;
    private javax.swing.JButton equalizeHistogramButton;
    private javax.swing.JButton equalizeHyperbolicLogarithmicButton;
    private javax.swing.JButton equalizeHyperbolicRootsButton;
    private javax.swing.JButton equalizeRayleighButton;
    private javax.swing.JButton equalizeUniformButton;
    private javax.swing.JButton exponentialNoiseButton;
    private javax.swing.JPanel filterPanel;
    private javax.swing.JButton freiChenButton;
    private javax.swing.JButton gammaNoiseButton;
    private javax.swing.JButton gaussianNoiseButton;
    private javax.swing.JButton geometricMeanFilterButton;
    private javax.swing.JButton gradientFirstOrderButton;
    private javax.swing.JButton grayButton;
    private javax.swing.JButton greaterThanButton;
    private javax.swing.JButton greaterThanButton1;
    private javax.swing.JButton greaterThanOrEqualButton;
    private javax.swing.JButton greenButton;
    private javax.swing.JButton harmonicMeanFilterButton;
    private javax.swing.JPanel histogramPanel;
    private javax.swing.JButton homogeneityOperatorButton;
    private javax.swing.JButton hsiButton1;
    private javax.swing.JButton hsiToRGBButton;
    private javax.swing.JButton hsvButton1;
    private javax.swing.JButton hsvToRGBButton;
    private javax.swing.JLabel imageLabel;
    private javax.swing.JScrollPane imageScrollPane;
    private javax.swing.JButton interpolationButton;
    private javax.swing.JButton invertBinButton;
    private javax.swing.JButton kirschButton;
    private javax.swing.JButton labToRGBButton;
    private javax.swing.JButton laplacianButton;
    private javax.swing.JPanel leftPanel;
    private javax.swing.JButton lessThanButton;
    private javax.swing.JButton lessThanButton1;
    private javax.swing.JButton lessThanOrEqualButton;
    private javax.swing.JButton lessThanOrEqualButton1;
    private javax.swing.JPanel linearFilterPanel;
    private javax.swing.JButton loadButton;
    private javax.swing.JButton matchHistogramButton;
    private javax.swing.JButton maxFilterButton;
    private javax.swing.JButton maxMinFilterButton;
    private javax.swing.JButton medianFilterButton1;
    private javax.swing.JButton midpointFilterButton;
    private javax.swing.JButton minFilterButton;
    private javax.swing.JPanel modHistogramPanel;
    private javax.swing.JButton modeFilterButton;
    private javax.swing.JButton multiplicationButton;
    private javax.swing.JPanel noisePanel;
    private javax.swing.JPanel nonlinearFilterPanel;
    private javax.swing.JButton notButton;
    private javax.swing.JButton notButton1;
    private javax.swing.JButton notEqualButton;
    private javax.swing.JPanel operationPanel;
    private javax.swing.JButton orButton;
    private javax.swing.JButton pepperNoiseButton;
    private javax.swing.JButton prewittButton;
    private javax.swing.JButton prewittSecondOrderButton;
    private javax.swing.JButton rayleighNoiseButton;
    private javax.swing.JButton redButton;
    private javax.swing.JButton resetButton;
    private javax.swing.JButton rgbToCMYButton;
    private javax.swing.JButton rgbToHSIButton;
    private javax.swing.JButton rgbToHSVButton;
    private javax.swing.JButton rgbToLabButton;
    private javax.swing.JButton rgbToYIQButton;
    private javax.swing.JTabbedPane rightPanel;
    private javax.swing.JButton rotationButton;
    private javax.swing.JButton saltNoiseButton;
    private javax.swing.JButton saltPepperNoiseButton;
    private javax.swing.JButton saveButton;
    private javax.swing.JButton scaleHistogramButton;
    private javax.swing.JButton shiftHistogramButton;
    private javax.swing.JButton showHistogramButton;
    private javax.swing.JPanel sliderPanel1;
    private javax.swing.JPanel sliderPanel2;
    private javax.swing.JButton sobelButton;
    private javax.swing.JButton subtractionButton;
    private javax.swing.JButton sumButton;
    private javax.swing.JPanel topPanel;
    private javax.swing.JButton translationButton;
    private javax.swing.JButton uniformNoiseButton;
    private javax.swing.JButton xorButton;
    private javax.swing.JButton yiqButton1;
    private javax.swing.JButton yiqToRGBButton;
    // End of variables declaration//GEN-END:variables
}
