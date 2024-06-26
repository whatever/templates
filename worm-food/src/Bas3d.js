import * as THREE from "three";

import {App} from "@pool-water/secret-sauce";

export class Bas3d extends App {
  constructor({el}) {
    super({el: el});

    this.el = el;

    this.clock = new THREE.Clock();

    this.ctx = el.getContext("webgl", {preserveDrawingBuffer: true});

    this.renderer = new THREE.WebGLRenderer({
      canvas: el,
      antialias: true,
    });

    this.camera = new THREE.PerspectiveCamera(
      80,
      window.innerWidth/window.innerHeight,
      0.1,
      1000,
    );

    this.renderer.setPixelRatio(window.devicePixelRation);

    this.renderer.setSize(el.width, el.height);

    this.scene = new THREE.Scene();
  }

  update() {
  }

  draw() {
    this.renderer.render(this.scene, this.camera);
  }

  setSize(w, h) {
    this.renderer.setSize(w, h);
    this.camera.aspect = w/h;
    this.camera.updateProjectionMatrix();
  }
}
