from pathlib import Path
import matplotlib.pyplot as plt
import mpl_fontkit as fk

if __name__ == "__main__":
    save_path = Path(__file__).parent
    fk.install("Lato")

    fig, ax = plt.subplots()
    fk.font_table("Lato", ax=ax)
    fig.savefig(save_path / "font_tables.svg")

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.text(.5, .5, "Lato Font", va="center", ha="center",
            fontdict={"style": "italic", "weight": 700, "size": 24})
    fig.savefig(save_path / "in_plot.svg")

    fig, ax = plt.subplots(figsize=(3, 3))
    fk.show("Lato", ax=ax)
    fig.savefig(save_path / "show.svg")

    fk.install_fontawesome()
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.text(.5, .5, "\uf58b\uf005\uf59b", ha="center", va="center",
            fontfamily="Font Awesome 6 Free", fontsize=20, color="#37306B",
            transform=ax.transAxes)
    ax.set_axis_off()
    fig.savefig(save_path / "fontawesome.svg")
