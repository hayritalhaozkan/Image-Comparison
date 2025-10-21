# Image Comparison

Bu proje, iki farklı tarihte çekilmiş görüntüleri yan yana kaydırmalı (slider) bir karşılaştırma arayüzü ile görselleştirmek için Streamlit tabanlı basit bir uygulama içerir. Uygulama, kullanıcının sol ve sağ görüntüleri yükleyip ortadaki kaydırıcıyı hareket ettirerek değişimleri görmesini sağlar.

## Özellikler
- İki görüntüyü yükleme (PNG, JPG, JPEG, TIF, TIFF desteklenir)
- Kaydırmalı karşılaştırma (mouse ile ortadaki çizgiyi hareket ettirerek gözlemleme)
- Sol/sağ etiketlerini sidebar üzerinden özelleştirme

## Deploy / Canlı Link


## Lokal olarak çalıştırma (macOS / zsh)
Aşağıdaki adımlar, projeyi yerel makinenizde çalıştırmak için yeterlidir.

1. Bir Python sanal ortamı oluşturun ve aktive edin (örnek: venv):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

3. Uygulamayı çalıştırın:

```bash
streamlit run slider_comparison.py
```

4. Tarayıcınız otomatik açılmazsa, terminalde görünen localhost linkini ziyaret edin.



## Bağımlılıklar
Bu proje aşağıdaki paketleri kullanır:

- streamlit
- streamlit-image-comparison
- pillow



