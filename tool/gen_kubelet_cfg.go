// package main

// DO NOT USE THIS FILE !!!
// COPY TYPE FROM "k8s.io/kubelet/config/v1beta1" DIRECTLLY !!!

// import (
// 	"fmt"

// 	yaml "gopkg.in/yaml.v2"
// 	"k8s.io/kubelet/config/v1beta1"
// 	// api "k8s.io/kubernetes/pkg/kubelet/apis/config/v1beta1"
// )

// func main() {
// 	// aaa := new(v1beta1.KubeletConfiguration)
// 	// aaa.FeatureGates = make(map[string]bool)
// 	// aaa.FeatureGates["abd"] = true
// 	// ccc, _ := yaml.Marshal(aaa)
// 	// fmt.Printf("%s", ccc)

// 	// fmt.Println("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

// 	// kc, _ := options.NewKubeletConfiguration()
// 	// kc.FeatureGates = make(map[string]bool)

// 	// // k2 := (*kc).(v1beta1.KubeletConfiguration)
// 	// dkc, _ := yaml.Marshal(kc)

// 	k2 := new(v1beta1.KubeletConfiguration)
// 	// api.SetDefaults_KubeletConfiguration(k2)
// 	// yaml.Unmarshal(dkc, k2)

// 	// kc := &v1beta1.KubeletConfiguration{}
// 	ddd, _ := yaml.Marshal(k2)
// 	// ddd, _ := json.Marshal(k2)
// 	fmt.Printf("%s", ddd)

// 	// fmt.Printf("%+v", k2)
// 	// ddd, _ := json.Marshal(kc)
// 	// aaa, _ := yaml.JSONToYAML(ddd)
// 	// fmt.Printf("%s", aaa)

// }

// // versioned := &v1beta1.KubeletConfiguration{}
// // scheme, _, err := scheme.NewSchemeAndCodecs()
// // if err != nil {
// // 	return
// // }
// // if err := scheme.Convert(kc, versioned, nil); err != nil {
// // 	return
// // }
// // // encode
// // encoder, err := newKubeletConfigJSONEncoder()
// // if err != nil {
// // 	return
// // }
// // data, err := runtime.Encode(encoder, versioned)
// // if err != nil {
// // 	return
// // }
// // create the directory, if it does not exist
// // dir := filepath.Dir(path)
// // if err := os.MkdirAll(dir, 0755); err != nil {
// // 	return err
// // }
// // // write the file
// // if err := ioutil.WriteFile(path, data, 0755); err != nil {
// // 	return err
// // }
// // return nil

// // 	io.write(data)
// // }

// // func newKubeletConfigJSONEncoder() (runtime.Encoder, error) {

// // 	_, kubeletCodecs, err := scheme.NewSchemeAndCodecs()
// // 	if err != nil {
// // 		return nil, err
// // 	}

// // 	mediaType := "application/json"
// // 	info, ok := runtime.SerializerInfoForMediaType(kubeletCodecs.SupportedMediaTypes(), mediaType)
// // 	if !ok {
// // 		return nil, fmt.Errorf("unsupported media type %q", mediaType)
// // 	}
// // 	return kubeletCodecs.EncoderForVersion(info.Serializer, v1beta1.SchemeGroupVersion), nil
// // }

// // func newSchemeAndCodecs() {

// // }
