def corr(data, cmap="viridis"):
    plt.figure(figsize=(30, 25))
    sns.heatmap(data, annot=True, cmap=cmap, fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix of Features', color="brown", size=20)
    plt.show()


def show_distribution(data, col):
    data = data.copy()
    col = str(col)

    mean = round(data[col].mean(), 4)
    std = round(data[col].std(), 4)
    mode = round(data[col].mode()[0], 4)
    var = round(np.sqrt(data[col].std()), 4)
    print("The mathemiocal distribution of the data are presented as follows: ")
    print(f"Mean:{mean} \nMode:{mode} \nStandard Deviation:{std} \nVariance:{var}")

    fig, ax = plt.subplots(1, 2, figsize=(10, 6))
    sns.histplot(data[col], ax=ax[0], binwidth=1, color="black")
    ax[0].axvline(mean, linewidth=2, linestyle="--", color="red", label="mean")
    ax[0].axvline(mode, linewidth=1, linestyle="--", color="orange", label="mode")
    ax[0].axvline(std, linewidth=1, linestyle="--", color="blue", label="standard deviation")
    ax[0].axvline(var, linewidth=1, linestyle="--", color="yellow", label="standard deviation")
    ax[0].set_title(f"Distribution Plot for {col}", color="brown")

    sns.boxplot(y=data[col], ax=ax[1], width=0.5, color="black")
    ax[1].axhline(mean, linewidth=2, linestyle="--", color="red", label="mean")
    ax[1].axhline(mode, linewidth=1, linestyle="--", color="orange", label="mode")
    ax[1].axhline(std, linewidth=1, linestyle="--", color="blue", label="standard deviation")
    ax[1].axhline(var, linewidth=1, linestyle="--", color="yellow", label="standard deviation")
    ax[1].set_title(f"Boxplot for {col}", color="brown")
    ax[1].legend(loc="upper left", bbox_to_anchor=(1, 1), fontsize=10)
    plt.show()


def show_unique_values(df, col):
    if df[col].nunique() < 5:
        plt.figure(figsize=(5,3))
        print(f"{'-' * 120}")
        print(f"{col}")
        print(f"{'-' * 120}")
        df[col].value_counts(ascending=True).plot(kind="bar", color="black")
        plt.xlabel(f"{col}")
        plt.xticks(rotation=0)
        plt.show()

    elif df[col].nunique() < 15:
        plt.figure(figsize=(10,8))
        print(f"{'-' * 120}")
        print(f"{col}")
        print(f"{'-' * 120}")
        df[col].value_counts(ascending=True).plot(kind="barh", color="black")
        plt.xlabel(f"{col}")
        plt.show()

    else:
        plt.figure(figsize=(10,4))
        print(f"{'-' * 120}")
        print(f"{col}")
        print(f"{'-' * 120}")
        df[col].value_counts().head(10).plot(kind="barh", color="black")
        plt.xlabel(f"{col}")
        plt.show()