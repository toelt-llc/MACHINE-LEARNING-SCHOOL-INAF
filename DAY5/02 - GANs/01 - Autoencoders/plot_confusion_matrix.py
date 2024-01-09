import seaborn as sns
import matplotlib.pyplot as plt

class plot_cm():

    def __init__(self):
        pass

    def plot_confmat(self, data, labels, output_filename):
        """
        Plots a confusion matrix using heatmap.

        Args:
            data (list of lists): list of lists with confusion matrix data.
            labels (list): labels which will be plotted across x and y axis.
            output_filename (str): path to output file.
        """

        sns.set(color_codes = True)
        sns.set(font_scale = 1.3)

        plt.figure(1, figsize = (9, 6))

        ax = sns.heatmap(data, annot = True, cmap = 'Blues', cbar_kws = {'label': 'Scale'}, fmt = 'd')

        ax.set_xticklabels(labels, fontsize = 16)
        ax.set_yticklabels(labels, fontsize = 16)

        ax.set_xlabel('Predicted Label', fontsize = 16)
        ax.set_xlabel('True Label', fontsize = 16)

        plt.savefig(output_filename, bbox_inches = 'tight', dpi = 300)
        plt.show()
        plt.close()